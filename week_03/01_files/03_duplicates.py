'''
In a large collection of MP3 files, there may be more than one copy of
the same song, stored in different directories or with different file
names. The goal of this exercise is to search for duplicates.

Write a program that searches a directory and all of its subdirectories,
recursively, and returns a list of complete paths for all files with a
given suffix (like .mp3). Hint: os.path provides several useful
functions for manipulating file and path names.

To recognize duplicates, you can use md5sum to compute a “checksum” for
each file. If two files have the same checksum, they probably have the
same contents. To double-check, you can use the Unix command diff.
Solution: http://thinkpython2.com/code/find_duplicates.py.

Go and tackle your duplicate files! :)

Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''
import os
import check_duplicates as checkdup

path = "/Users/Ming/Documents/Omneia"
file_list = []
res_list = []
#path = "/Users/Ming/Documents/CodingNomads/"
try:
    for d in [x[0] for x in os.walk(path)]:
        try:
            for i in os.listdir(d):
                if i.split(".")[1] == "pdf":
                    file = os.path.join(d, i)
                    file_list.append(file)
                    #print(file)
                    #print(checkdup.compute_checksum(file))
                    res_list.append(checkdup.compute_checksum(file))
        except IndexError:
            pass
except IndexError:
    print("No folder like that.")

#print(checkdup.check_pairs(file_list))
d = checkdup.compute_checksums(path, suffix='.pdf')
# checkdup.print_duplicates(d)
d = {}
l = []
for i in res_list:
    x=i[0].split()
    d[x[1]]= x[0]
print(d)

for k1, v1 in d.items():
    v = v1
    k = k1
    for k2, v2 in d.items():
        if v == v2 and k != k2:
            l.append(k)
            l.append(k2)
print("Duplicates are: \n",set(l))

