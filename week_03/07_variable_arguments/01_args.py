'''
Write a script with a function that demonstrates the use of *args.

'''


def initials(*args):
    # for x in args:
    #     c += x[0].upper()
    # return c
    d = "".join(x[0].upper() for x in args)
    return d


print(initials("ubud", "bali", "indonesia"))
