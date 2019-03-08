'''
Write a script that generates an exception. Handle this exception with a try/except.
For example:

list_ = ["hello world!"]
print(list_[1])

This raises and exception that needs to be handled.

'''
import math

try:
    ans = float(input("Enter a number please: "))
    print(math.log10(ans))
except TypeError as err:
    print(f"Number ONLY!: {err}")
except ValueError as fnf:
    print(f"Not valid, please enter another number!: {fnf}")
