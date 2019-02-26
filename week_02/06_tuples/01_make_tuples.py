'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple
Notes:

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

'''
try:
    num_list = input("Please enter some numbers and separate them by comma ',':").split(",")
    print(num_list)
    for i in num_list:
        i = float(i)
except TypeError:
    print("Please make sure you enter only numbers")


num_list.sort()
if len((num_list)) % 2 != 0:
    num_list.append(0)
print(num_list)
result = []
for i in range(int(len(num_list) / 2)):
    tup = []
    for j in range(2):
        tup.append(num_list[j + i * 2])
    result.append(tuple(tup))

print(result)
