'''
Sum up all elements from the nested list of integers below.

'''

list_ = [1, 2, [10, 11], [42, 3], 9]

s = 0

for i in list_:
    if isinstance(i, list):
        for j in i:
            s += j
    else:
        s += i

print(s)
