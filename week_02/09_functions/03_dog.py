'''
Write a program with the following three functions:

    - bark - this function should not take in any arguments and should print the string "bark bark"
    - eat - takes in parameters food_item and amount and prints out "The dog ate <amount> of <food_item>
    - sleep - calls the python sleep method to sleep the program for 5 seconds.

'''
import time
def bark():
    return "bark bark"


def eat(food_item, amount):
    return f"The dog ate {amount} of {food_item}."


def sleep():
    time.sleep(5)

# The following program does the following: if you don't feed the dog, it will bark
# if you do, it will sleep for 5 mins
flag = True
while flag:
    bark()
    ans = input("Do you want to feed the dog (yes/no):")
    if ans == 'yes':
        food = input("What do you want to feed the dog?")
        quant = input("How much would you like?")
        print(eat(food, quant))
        print("Time to sleep, maybe? hmhnhnn")
        sleep()
        print("Yes! Thank you!")
        flag = False
    else:
        continue






