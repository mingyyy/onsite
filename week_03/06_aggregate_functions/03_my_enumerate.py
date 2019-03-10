'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''


def my_enumerate(*args, num=0):
    y = 0
    x_list = {}
    for x in args:
        y += 1+num
        x_list[y] = x
    yield x_list


for x in my_enumerate("Ubud", "Kuta", "Canggu", 5, "888", num=1000):
    for k, v in x.items():
        print(f"{k}. {v}")
