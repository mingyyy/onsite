'''
Build a simple aggregator function.

'''
# aggregate things together. e.g. sum of list of numbers
# combination of list of strings.


def collection(*args):
    c = ""
    for x in args:
        c += str(x).swapcase()
    return c


print(collection("Ubud", "Bali", "Indonesia"))
