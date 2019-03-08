'''
Write a function that takes in a list and finds the max, min, average and sum.

'''


def stat(l):
    """
    This function takes in a list and find some statistics for the numbers.
    :param l: a list of numbers
    :return: the max, min, mean and sum of the numbers in the list
    """

    # chained assignment should be avoided: maxi = mini = avg = summ = 0.0

    maxi, mini, avg, summ = 0.0, 0.0, 0.0, 0.0
    for i in l:
        maxi = mini = i
        if i > maxi:
            maxi = i
        elif i < mini:
            mini = i
        summ += i
    avg = summ / len(l)
    return maxi, mini, avg, summ


print(stat([1,2,3,4,5]))
