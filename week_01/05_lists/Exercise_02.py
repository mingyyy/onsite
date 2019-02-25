'''
Given the two lists below, find the elements that are the same
and put them in a new list.
Put the elements that are different in another list.

Print both.

'''

list_one = [0, 4, 6, 18, 25, 42, 100]
list_two = [1, 4, 9, 24, 42, 88, 99, 100]

common_list = []
other_list = []
for i in list_one:
    if i in list_two:
        common_list.append(i)
    else:
        other_list.append(i)
for i in list_two:
    if i not in list_one:
        other_list.append(i)

print(common_list)
print(other_list)