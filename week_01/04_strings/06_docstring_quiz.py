'''
The following functions are all intended to check whether a string
contains any lowercase letters, but at least some of them are wrong.
For each function, write its docstring to describe what the function
actually does (assuming that the parameter is a string).

'''


def any_lowercase1(s):
    '''This function returns True if your string is in lower cases (you can have other signs) , otherwise False.
       There will be an error message if your input is not iterable.
    '''
    for c in s:
        if c.islower():
            return True
        else:
            return False


print(any_lowercase1("What a day")) # False
print(any_lowercase1("what a day!")) # True
print(any_lowercase1(("a","b")))


def any_lowercase2(s):
    '''This function returns True always because it's checking if 'c' is in lower case, which is always True.
    '''
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

print("")
print(any_lowercase2("W")) # True
print(any_lowercase2("LOVE")) # True
print(any_lowercase2(("a","b"))) # True


def any_lowercase3(s):
    '''This function returns True if your string contains lower cases, otherwise False.
       There will be an error message if your input is not iterable.
    '''
    for c in s:
        flag = c.islower()
    return flag

print("")
print(any_lowercase3("What a day")) # True
print(any_lowercase3("WHAT?")) # False


def any_lowercase4(s):
    '''This function returns True if your string contains lower cases, otherwise False.
       There will be an error message if your input is not iterable.
    '''
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


print("")
print(any_lowercase4("What a day"))
print(any_lowercase4("WHTA"))


def any_lowercase5(s):
    '''This function returns True if your string contains ONLY lower cases not even spaces, otherwise False.
       There will be an error message if your input is not iterable.
    '''
    for c in s:
        if not c.islower():
            return False
    return True

print("")
print(any_lowercase5("What a day")) # False
print(any_lowercase5("WHTA")) # False
print(any_lowercase5("what a day")) # False
print(any_lowercase5("day")) # True