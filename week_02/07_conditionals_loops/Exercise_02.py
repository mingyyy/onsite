'''
Take in a number from the user and print "Monday", "Tuesday", ...
"Sunday", or "Other" if the number from the user is 1, 2,... 7,
or other respectively. Use a "nested-if" statement.

'''

user_input = int(input("Enter an integer here, please:"))
dates_list = ['Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','Other']

if user_input in range(8):
    print(dates_list[user_input-1])
else:
    print(dates_list[7])
