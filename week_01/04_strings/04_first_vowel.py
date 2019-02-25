'''
Write a script that finds the first vowel in a user inputted string.

'''


find_vowel = str(input("Please enter something here, so we can find the vowels in it: ")).lower()

# if we define vowels as "a, e, o, i, u" only
vowels =['a','e','i','o','u']
n = 0

# method 1
for i in find_vowel:
    n += 1
    for j in vowels:
        while i == j:
            print(f"The first vowel is at {n} place and it is '{j}'.")
            exit()

if n==len(find_vowel):
    print("Sorry, there is no vowel in your input.")


# method 2
for i in find_vowel:
    n += 1
    if i in vowels:
        print(f"The first vowel is at {n} place and it is '{i}'.")
        exit()

if n==len(find_vowel):
    print("Sorry, there is no vowel in your input.")
