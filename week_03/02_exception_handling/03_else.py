'''
Write a script that demonstrates a try/except/else.

'''

a = 1
b = 0

try:
    c = a / b
except ZeroDivisionError:
    print("Denominator can't be zero.")
else:
    print(c)
finally:
    print("You still have a lot of homework to do!")
