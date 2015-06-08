#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """

    import heapq

    cleaned_data = []
    complete_data = []
    errors = []

    for i in range(90):
        complete_data.append( (ages[i], net_worths[i], abs(predictions[i]) - abs(net_worths[i])) )
        errors.append(complete_data[i][2])

    good_ones = heapq.nsmallest(81, errors)

    for entry in complete_data:
        if entry[2] in good_ones:
            cleaned_data.append(entry)

    return cleaned_data
