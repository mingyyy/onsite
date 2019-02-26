'''
Write a script that prints out all the squares of numbers
from a user inputed lower to a user inputed upper bound.

Use a for loop that demonstrates the use of the range function.

'''
l = int(input("Please enter an integer as your lower bound: "))
u = int(input("Please enter an integer as your upper bound: "))

if l > u:
    print("You lower bound is larger than your upper bound. Please re-enter. ")
else:
    for i in range(l, u+1, 1):
        print(i, i**2)
