'''
--------------------------------------------------------
                PROGRAMMED SONG LYRICS
--------------------------------------------------------

Programmatically create your own song lyrics with multiple verses,
interlaced with a repeating chorus.

Train using string methods and loops on an open-end mini-project!

- use one block of text as verse input (hint: linebreaks can be helpful!)
- use a for loop for creating the full lyrics

'''


def inbetween(num):
    return 'me gustas numero ' + str(num) + ", me gustaas tu"

verse_repeat = '''me gustas el cielo, me gustas tu
me gustas el mar, megustas tu 
me gustas llorar, megustas tu
me gustas pealar, megustas tu
me gustas el cine, megustas tu
me gustas la musica, megustas tu
'''
verse_repeat = verse_repeat.title()
for i in range(3):
    print(inbetween(i+1) + "\n")
    print(verse_repeat)
print("Hahahahahahahahaha...\nLalalalalalalalala.....")