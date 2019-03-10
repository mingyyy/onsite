'''
Re-write the following listcomp as a lambda expression.

'''

names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']
print([x.startswith('D') for x in names])

# get_d = lambda x: x.startswith('D')
# for i in names:
#     print(get_d(i))

print(list(map(lambda x: x.startswith('D'), names)))

