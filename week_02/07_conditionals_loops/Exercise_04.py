'''
Print out every prime number between 1 and 100.

'''
# prime numbers are only divisiable by itself and 1.

l = [2]
for i in range(1, 101, 2):
    n = 1
    for j in range(1, i+1, 1):
        if i % j != 0:
            n += 1
    if n+1 == i:
        l.append(i)


print(f"There are {len(l)} prime numbers between 1 and 100:")
print(l)