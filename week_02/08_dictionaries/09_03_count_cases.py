'''
Write a script that takes a sentence from the user and returns:

- the number of lower case letters
- the number of uppercase letters
- the number of punctuations characters
- the total number of characters

Use a dictionary to store the count of each of the above.
Note: ignore all spaces.

Example input:
    I love to work with dictionaries!
Example output:
    Upper case: 1
    Lower case: 26
    Punctuation: 1

'''

user = input("Please enter a string here: ")
l = u = p = t = s = 0
for i in user:
    if i.islower() == True:
        l += 1
    elif i.isupper() == True:
        u += 1
    elif i == "!":
        p += 1
    elif i == " ":
        s += 1
    t += 1

print(l, u, p, t-s)













