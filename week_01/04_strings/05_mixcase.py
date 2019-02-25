'''
Write a script that takes a user inputted string
and prints it out in the following three formats.
    - All letters capitalized.
    - All letters lower case.
    - All vowels lower case and all consonants upper case.

'''

user_input = input("Please tell me something, so I can print it out for you: ")

# All letters capitalized
print(user_input.title())

# All letters lower case.
print(user_input.lower())

# All vowels lower case and all consonants upper case.

s = str(input("Please tell me something, so I can print all vowels in lower case "
                   "and all consonants in upper case: ")).upper()

# if we define vowels as "a, e, o, i, u" only
vowels = ['A', 'E', 'I', 'O', 'U']
ilist = []
n = 0
for i in s:
    n += 1
    if i in vowels:
        ilist.append(i.lower())
    else:
        ilist.append(i)

print("".join(ilist))