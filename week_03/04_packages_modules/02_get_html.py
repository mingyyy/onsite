'''
In 3 lines of code, fetch the HTML text from codingnomads' main page
and print it to your console.

TIP:
- if you wonder what to use, google something like
    "most popular python package"
- if you run into encoding/decoding errors, you're experiencing something
    very common. head over to SO and find a solution!

'''

import html2text
import urllib.request

h = html2text.HTML2Text()
h.ignore_links = True
fp = urllib.request.urlopen("http://www.google.com").read() # http://codingnomads.co (pas bon)
print(h.handle(fp.decode("utf8")))
fp.close()

# Ignore converting links from HTML
# h.ignore_links = True
# print(h.handle("<p>Hello, <a href='http://earth.google.com/'>world</a>!"))




