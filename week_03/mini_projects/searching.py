'''
Write a script that searches a folder (and all its subfolders) on your computer and compiles a list of all of
all .jpg files (with the complete path of the files).

If you are feeling bold, create a list for each kind of file extension you find in the folder.

Start with a small folder to make it easy to check if your program is working correctly. Then sub out the
folder name with a bigger folder. This program should work for any specified folder on your computer.


'''

import os

path = "/Users/Ming/Documents/Omneia"

alist = []
# finding all the possible suffix store them in alist
try:
    for d in [x[0] for x in os.walk(path)]:
        try:
            for i in os.listdir(d):
                alist.append(i.split(".")[1].lower())
        except IndexError:
            pass
except IndexError:
    print("No folder like that.")

alist = set(alist)
# look for files based on alist.
try:
    for d in [x[0] for x in os.walk(path)]:
        try:
            for j in alist:
                print(f"{j} has the following:")
                for i in os.listdir(d):
                    if i.split(".")[1].lower() == j:
                        print(d + "/" + i)
        except IndexError:
            pass
except IndexError:
    print("No folder like that.")
