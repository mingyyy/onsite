'''
--------------------------------------------------------
                RANDOM HASHTAG GENERATOR
--------------------------------------------------------

Programmatically generate random hashtags by picking from a word list.

Tip: In UNIX systems you can access a dictionary file at this path:
        /usr/share/dict/words

'''

def Random_HashTag(word):
    '''
    This function generate some random HashTags based on your input
    :param w: any english word
    :return: A list of Hashtags
    '''
    wordlist = [line.strip() for line in open('/usr/share/dict/words')]
    # wl = open('/usr/share/dict/words', 'r')
    # wordlist = wl.readlines()
    # wl.close()
    w = []
    for x in wordlist:
        # if x[:len(word)] == str(word):
        #     w.append("#" + str(x))
        # elif x[-len(word):] == str(word):
        #     w.append("#" + str(x))
        if word in x:
            w.append("#" + x)
    return w

print(Random_HashTag("caden"))
print(Random_HashTag("martin"))