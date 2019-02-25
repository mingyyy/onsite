'''
A Caesar cypher is a weak form of encryption that involves “rotating”
each letter by a fixed number of places. To rotate a letter means to
shift it through the alphabet, wrapping around to the beginning if
necessary, so ’A’ rotated by 3 is ’D’ and ’Z’ rotated by 1 is ’A’.

To rotate a word, rotate each letter by the same amount. For example,
“cheer” rotated by 7 is “jolly” and “melon” rotated by -10 is “cubed”.
In the movie 2001: A Space Odyssey, the ship computer is called HAL,
which is IBM rotated by -1.

Write a function called rotate_word that takes a string and an integer
as parameters, and returns a new string that contains the letters from
the original string rotated by the given amount.

You might want to use the built-in function ord, which converts a
character to a numeric code, and chr, which converts numeric codes to
characters. Letters of the alphabet are encoded in alphabetical order,
so for example:

 ord('c') - ord('a')
2

Because 'c' is the two-eth letter of the alphabet. But beware:
the numeric codes for upper case letters are different.

Potentially offensive jokes on the Internet are sometimes encoded in
ROT13, which is a Caesar cypher with rotation 13. If you are not easily
offended, find and decode some of them.

'''
alpha = "abcdefghijklmnopqrstuvwxyz"

for i in alpha:
    print(i, ord(i), chr(ord(i)))


def rotate_word(message, num):
    """This function takes in two parameters
    :param message is the message you want to rotate
    :param num is how many alphabet you want to move forward
    """
    cypher = []
    num = int(num)
    for i in message.lower():
        if num >= 26:
            num = num % 26
        elif num <= -26:
            num = -(abs(num) % 26) # or -(-num%26)

        if 122 >= num + ord(i) >= 97:
            cypher.append(chr(ord(i) + num))
        elif num + ord(i) < 97:
            cypher.append(chr(ord(i) + 26 + num))
        else:
            cypher.append(chr(ord(i) - 26 + num))

    result = "".join(cypher)
    return print(result)


rotate_word("Abc", -28)
rotate_word("Abc", -27)
rotate_word("Abc", -2)
rotate_word("Abc", -1)

rotate_word("Abc", 29)
rotate_word("Abc", 30)
rotate_word("Abc", 3)
rotate_word("Abc", 4)