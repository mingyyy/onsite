'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''
x=[]
n = 0
with open("words.txt", "r") as f:
    for line in f.readlines():
        x.append(line)
        n += 1

with open("words_reverse.txt", "w") as fout:
    for i in range(n):
        fout.writelines(x.pop())

