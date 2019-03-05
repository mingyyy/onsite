'''
Write a program that reads in the file words.txt and prints only the
words with more than 20 characters (not counting whitespace).

Source: http://greenteapress.com/thinkpython2/html/thinkpython2010.html

'''
with open("words.txt") as file_object:
    for line in file_object:
        if len(line.strip()) >= 20:
            print(line)

# f=open("new.txt")
# stat= f.close()
# assert stat is None

