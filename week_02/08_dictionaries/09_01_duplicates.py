'''
Using a dictionary, write a function called has_duplicates that takes
a list and returns True if there is any element that appears more than
once.
'''


def has_duplicates(l):
    '''
    This function takes in a list
    :return: True if there is any element duplicated
    '''
    d = {}
    for i in l:
        d[i] = 0
    if len(d) != len(l):
        return True


l = [1,2,3,4,5,3]
print(has_duplicates(l))






