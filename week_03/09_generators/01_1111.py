'''
Create a Generator that loops over the given sequence and prints out
only the items that are divisible by 1111.

'''

# note: range() also works with a generator object internally
nums = range(1, 1000000)
gen = (x for x in nums if x % 1111 == 0)
print(gen)
for i in gen:
    print(i)