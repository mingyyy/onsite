'''
--------------------------------------------------------
                99 BOTTLES OF BEER LYRICS
--------------------------------------------------------

https://www.reddit.com/r/beginnerprojects/comments/19kxre/project_99_bottles_of_beer_on_the_wall_lyrics/

-- GOAL --
Create a program that prints out every line to the song
"99 bottles of beer on the wall." This should be a pretty simple program,
so to make it a bit harder, here are some rules to follow.

-- RULES --
1) If you are going to use a list for all of the numbers,
    do not manually type them all in. Instead, use a built in function.
    MY: ord("c") is 99
2) Besides the phrase "take one down," you may not type in any
    numbers/names of numbers directly into your song lyrics.
3) Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
4) Put a blank line between each verse of the song.

'''
num = ord("c")


def repeat(n):
    if num-n-1 == 0:
        return str(num-n) + " bottle of beer on the wall, " + str(num-n) + " bottle of beer.\n" \
         "Take one down and pass it around, no more bottles of beer on the wall."
    elif num-n-1 == 1:
        return str(num-n) + " bottles of beer on the wall, " + str(num-n) + " bottles of beer.\n" \
         "Take one down and pass it around, " + str(num-n-1) + " bottle of beer on the wall."
    else:
        return str(num-n) + " bottles of beer on the wall, " + str(num-n) + " bottles of beer.\n " \
         "Take one down and pass it around, " + str(num-n-1) + \
         " bottles of beer on the wall."


for i in range(num):
    print(repeat(i),"\n")
print("No more bottles of beer on the wall, no more bottles of beer. \n"
      "Go to the store and buy some more, " + str(num) + " bottles of beer on the wall.")


