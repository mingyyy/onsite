'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.

'''
shortest = []
longest = []
n = 0
with open("words.txt") as f:
    for line in f.readlines():
        n += 1
        if n == 1:
            shortest.append(line.strip())
            longest.append(line.strip())
        if len(line.strip()) < len(shortest[0]):
            shortest = []
            shortest[0] = line.strip()
        elif len(line.strip()) == len(shortest[0]) and line.strip() != shortest[0]:
            shortest.append(line.strip())
        if len(line.strip()) > len(longest[0]):
            longest = []
            longest.append(line.strip())
        elif len(line.strip()) == len(longest[0]) and line.strip() != longest[0]:
            longest.append(line.strip())
print(shortest)
print(longest)
print(f"In total {n} words.")
