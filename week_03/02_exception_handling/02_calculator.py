'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''
try:
    ans = input("Please enter two numbers, separated by comma:").split(",")
    a, b = ans
    a = int(a)
    b = int(b)
    c = a/b
except ZeroDivisionError:
    print("can't divide by zero!")
except ValueError:
    print("Number ONlY!")
