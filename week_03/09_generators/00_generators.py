'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''
my_num = [1, 34, 545, 3, 13, 34]
gen = (x**(1/2) for x in my_num)
print(gen)
for i in gen:
    print(i)
