'''
Take in 10 numbers from the user. Place the numbers in a list.
Using the loop of your choice, calculate the sum of all of the
numbers in the list as well as the average.

Print the results.

'''

user_input = input("Please enter 10 numbers, separate them by commas: ").split(",")
print(type(user_input))

"""takes in a list of numbers, and then return the sum and avg of the numbers."""
summation = 0
avg = 0
n = len(user_input)
for i in user_input:
    summation += float(i)

avg = summation/n
print(summation, avg)


