'''
Create a new dictionary using the three dictionaries below.
Then print out each key-value pair.

'''


dict_1 = {1: 1, 2: 4}
dict_2 = {3: 9, 4: 16}
dict_3 = {5: 25, 6: 36, 7: 49}

dict_combine={}
for a, b in dict_1.items():
    dict_combine[a] = b
for a, b in dict_2.items():
    dict_combine[a] = b
for a, b in dict_3.items():
    dict_combine[a] = b

for a in dict_combine:
    print(a, dict_combine[a])
