'''
Using the JavaScript support in requests_html, parse the contents of
an Instagram page you are interested in.

Fetch and prepare all the image links - and only the image links!
* How can you exclude other links present on the page?
* BONUS: Can you find a way to download those images and save them to
         your computer using python?

'''

from requests_html import HTMLSession
from requests_html import HTML
import re
import time
import urllib



url = "https://www.instagram.com/hectorretamalphotographer"
session = HTMLSession()
ins = session.get(url)
ins.html.render()

with open("photo_links.txt", "w") as f:
    for i in ins.html.absolute_links:
        if re.search(r'/p/', str(i)):
            f.write(f"{i}\n")

with open("photo_links.txt", "r") as f:
    lines = f.readlines()
    for urlf in lines:
        name = urlf.split("/")[4]
        # print(name)
        session = HTMLSession()
        photo = session.get(urlf)
        photo.html.render()
        time.sleep(1.5)

        x = photo.html.find(".FFVAD")
        for i in x:
            y = str(i).split('src')[1]
        foto_link = y[2:].strip()
        getf = session.get(foto_link[:-1])
        with open(name + ".jpeg", 'wb') as file:
            file.write(getf.content)
