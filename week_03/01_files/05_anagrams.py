'''
Download http://thinkpython2.com/code/anagram_sets.py.
You’ll see that it creates a dictionary that maps from a sorted string
of letters to the list of words that can be spelled with those letters.
For example, 'opst' maps to the list:
['opts', 'post', 'pots', 'spot', 'stop', 'tops'].

Write a module that imports anagram_sets and provides two new functions:
store_anagrams should store the anagram dictionary in a “shelf”;
read_anagrams should look up a word and return a list of its anagrams.
Solution: http://thinkpython2.com/code/anagram_db.py.


Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''
import shelve
import sys

import anagram_sets as a
import anagram_db as adb

def store_anagrams(word, anagram_map):

    """Stores the anagrams from a dictionary in a shelf.

    filename: string word of shelf
    anagram_map: dictionary that maps strings to list of anagrams
    """
    shelf = shelve.open(word, 'c')

    for word, word_list in anagram_map.items():
        shelf[word] = word_list

    shelf.close()


def read_anagrams(word):
    #return list_anagrams

    """Finds anagrams for a word.

    filename: word

    Returns: a map from each word to a list of its anagrams.
    """
    d = {}

    word = word.strip().lower()
    t = a.signature(word)
    print(t)

    # TODO: rewrite using default dict
    if t not in d:
        d[t] = [word]
    else:
        d[t].append(word)
    return d


print(read_anagrams("post"))