'''
Re-write the following listcomp as a lambda expression.

'''

names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']
print([x.startswith('D') for x in names])

get_D = lambda x: x.startswith('D')
for i in names:
    print(get_D(i))
