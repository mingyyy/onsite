'''
Read in the first number from 'integers.txt' and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''
import math


try:
    with open("integers.txt") as f:
        try:
            x = int(f.readline())
        except ValueError:
            print("It should be a number! Check the file.")
        else:
            print(math.log10(x))
except IOError:
    print("Can't open it. YOu don't have permission.")
