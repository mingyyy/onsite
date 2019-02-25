'''
There is a string method called 'count' that is similar to the following
code:

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

Read the documentation of the 'count' method and write an invocation that
counts the number of a’s in 'banana' that uses the in-built 'count'.
'''

word = 'banana'
print(word.count("a"))

word = "elefante"
c = word.count("e", 0, 3)
print(f"From the word {word}, there are {c} 'e' in the first 4 places.")
