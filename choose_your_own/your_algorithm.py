#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
'''
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
'''
#################################################################################

## ---- KNN ---- ##
'''
from sklearn import neighbors
from sklearn.metrics import accuracy_score

n_n = 2

clf = neighbors.KNeighborsClassifier(n_n)
clf.fit(features_train, labels_train)
'''


## ---- RANDOM FOREST ---- ##
'''
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

clf = RandomForestClassifier(n_estimators=15, min_samples_split=40)
clf.fit(features_train, labels_train)
'''

## ---- ADABOOST ----##
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score

clf = AdaBoostClassifier(n_estimators=25, learning_rate=1.5)
clf.fit(features_train, labels_train)


pred = clf.predict(features_test)
print accuracy_score(labels_test, pred)


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
