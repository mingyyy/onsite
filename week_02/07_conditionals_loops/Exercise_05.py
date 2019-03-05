'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound. Also, calculate the average of numbers.
	Print the results to the console.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
		The average is: 50.5
'''

input_u = int(input("Please enter an integer as the upper bound:"))
input_l = int(input("Please enter an integer as the lower bound:"))
s = 0

if input_u < input_l:
    print("You upper bound is smaller than your lower bound, please re-enter!")
else:
    for i in range(input_l, input_u+1, 1):
        s += i
    print(f"The sum is: {s}")
    print(f"The average is: {s/(input_u-input_l+1)}")
