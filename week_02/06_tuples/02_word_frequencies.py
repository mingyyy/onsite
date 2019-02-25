'''
Write a function called most_frequent that takes a string and prints
the letters in decreasing order of frequency.

For example, the follow string should produce the following result.

string_ = 'hello'

Output:
l, h, e, o

For letters that are the same frequency, the order does not matter.

'''


def most_frequent(user_str):
    ''' This funciton takes in one variable: a string and returns the letters in descending order of frequency
    :param any string
    :result ordered based on frequency
    '''


    temp = list(set(user_str))
    counter = []
    for i in range(len(temp)):
        temp[i]= str(user_str.count(temp[i])) + temp[i]

    temp.sort()
    temp.reverse()

    for i in range(len(temp)):
        temp[i] = temp[i][-1:]

    result = ""
    for i in temp:
        result += (i + ", ")
    result = result.rstrip(", ")

    print(result)

most_frequent("hello")
most_frequent("ana")