'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''
flag = True
while flag is True:
    ans = input("Enter an integer:")
    try:
        print(int(ans))
        flag = False
    except ValueError:
        print("Sorry, not an integer. Please re-enter.")
