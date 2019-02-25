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
    number_list = input("Please enter some numbers and separate them by comma ',':").split(",")
    print(number_list)

except TypeError:
    print("Please make sure you enter only numbers")

if len((number_list)) % 2 != 0:
    number_list.append(0)

new_list = []
for i in number_list:
    new_list.append(float(i))

new_list.sort()
print(new_list)
result = []
for i in range(int(len(new_list)/2)):
    tup = []
    for j in range(2):
        tup.append(new_list[j + i * 2])
    result.append(tuple(tup))

print(result)



