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
adirectory = {}
# finding all the possible suffix store them in alist
try:
    for d in [x[0] for x in os.walk(path)]:
        try:
            for i in os.listdir(d):
                extension = i.split(".")[1].lower()
                if extension in alist:
                    adirectory[extension] += ", " + os.path.join(d, i)
                else:
                    alist.append(extension)
                    adirectory[extension] = os.path.join(d, i)
                extension = ""
        except IndexError:
            pass
except IndexError:
    print("No folder like that.")

print("list of extensions:", set(alist))
for key, value in adirectory.items():
    print(f"\nFor extension .{key}, the following files have been found under the path: ")
    for file in value.split(","):
        print(file.strip())

# look for files based on alist. Somehow os.walk again won't show the sub-directory anymore???

# try:
#     for j in alist:
#         print(j)
#         try:
#             for dire in [y[0] for y in os.walk(path)]:
#                 # print(f"You have the following files with the extension .{j.upper()} under {dire}:")
#                 for item in os.listdir(dire):
#                     if item.split(".")[1].lower() == j:
#                         print(os.path.join(dire,item))
#         except IndexError:
#             print("---")
# except IndexError:
#     print("please check your list of extensions.")
