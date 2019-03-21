'''
Using the Chuck Norris API in combination with the datamuse API
( https://api.chucknorris.io/ - https://www.datamuse.com/api/ )

* Query the chucknorris api for a sentence
* Use the last word of that sentence to send a query to the Datamuse API
  and use the rel_rhy (or rel_nry) query parameter to fetch a word that rhymes
* Repeat a coupe of times and store the sentences and rhyme words
* Synthesize the collected results into an avant-garde poem and present it to class ;)

'''
import requests
import re
url_cn = "https://api.chucknorris.io/jokes/random"
url_dm = "https://api.datamuse.com/words?rel_rhy="

loop_times = 10
# loop trough the process
for x in range(loop_times):
    # chucknorris sentence
    cn = requests.get(url_cn).text # todo try out JSON format, check if the /u0027 problem persist
    txt = cn.split('":"')[-1]
    # handle \u0027 like things in a string: transfer to bytes and then back to string.
    sentence = re.sub(r'\\u*')
    # print(txt)
    # sentence = "".join(chr(x) for x in txt)
    print(sentence)
    last = sentence.split()[-1]
    lastword = re.findall("\w+", last)[0]
    print(lastword)

    # Datamuse query for rhyme words from last word of chucknorris
    url_dm += str(lastword)
    dm = requests.get(url_dm)
    url_dm = "https://api.datamuse.com/words?rel_rhy="
    rhy = ""
    for i in dm.json():
        rhy += i["word"] + " "
    with open("synthesize.txt", "a") as f:
        f.write(str(x+1) + ". " + sentence + "\n")
        f.write(lastword + ": " + rhy + "\n")

# poem!

