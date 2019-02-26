'''
Write a program that gets a number between 1 and 1,000,000,000
from the user and determines whether it is odd or even using an if statement.
Print the result.

NOTE: We will be using the input() function. This is demonstrated below.

'''

user_input = float(input("Enter a number between 1 and 1,000,000,000 please:"))

try:
    if user_input % 2 == 0:
        print("This is an even number.")
    else:
        print("This is an odd number.")

except TypeError:
    print("Please re-enter! This is not a number")
