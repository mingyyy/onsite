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
    ''' This function takes in one variable: a string and returns the letters in descending order of frequency
    :param user_str as a string
    :result ordered based on frequency
    '''

    temp = list(set(user_str))
    for i in range(len(temp)):
        temp[i] = str(user_str.count(temp[i])) + temp[i]
    temp.sort(reverse=True)
    temp = [temp[i][-1:] for i in range(len(temp))]
    result = ""
    for i in temp:
        result += (i + ", ")
    return result.rstrip(", ")


print(most_frequent("hello"))
print(most_frequent("motivation"))
