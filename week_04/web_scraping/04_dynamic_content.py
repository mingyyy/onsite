'''
Using the JavaScript support in requests_html, parse the contents of
an Instagram page you are interested in.

Fetch and prepare all the image links - and only the image links!
* How can you exclude other links present on the page?
* BONUS: Can you find a way to download those images and save them to
         your computer using python?

'''

from requests_html import HTMLSession
import re
from io import open as iopen


# url = "https://www.instagram.com/hectorretamalphotographer"
# session = HTMLSession()
# ins = session.get(url)
# ins.html.render()
#
# with open("photo_links.txt", "w") as f:
#     for i in ins.html.absolute_links:
#         if re.search(r'/p/',str(i)):
#             f.write(f"{i}\n")

urlf="https://www.instagram.com/p/Bt8wH2cji7q/"
session = HTMLSession()
photo = session.get(urlf)
photo.html.render()

with iopen("fotos", 'wb') as file:
    file.write(photo.content)