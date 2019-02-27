'''
--------------------------------------------------------
                GUESS THE RANDOM NUMBER
--------------------------------------------------------

Build a Guess-the-number game that asks a player for an input until they
pick the correct (randomly generated) number between 1 and 100.

Tip: Use python's 'random' module.

'''
import random
flag = True
guess = 100
while flag:
    user_input = input(f"Please guess a number between 1 and {guess}: ")
    ans = random.randint(1, guess)
    counter = 0
    if int(user_input) == ans:
        print("You won!")
        flag = False
    else:
        continue
