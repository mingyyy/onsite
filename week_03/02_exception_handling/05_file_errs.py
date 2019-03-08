'''
Read in the first number from 'integers.txt' and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''
import math

try:
    with open("integers5.txt") as f:
        try:
            x = int(f.readline())
        except ValueError:
            print("It should be a number! Check the file.")
        else:
            print(math.log10(x))
except FileNotFoundError as err:
    print(err)
except IOError:
    print("Can't open it. You don't have permission.")
