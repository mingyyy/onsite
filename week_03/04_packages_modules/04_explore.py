'''
Do some research on other popular python packages and what the are used for. Feel free to import them
and play around a little.

'''
# from lxml import html
# import requests
#
# page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
# tree = html.fromstring(page.content)
#
# # This will create a list of buyers:
# buyers = tree.xpath('//div[@title="buyer-name"]/text()')
# # This will create a list of prices
# prices = tree.xpath('//span[@class="item-price"]/text()')
#
# print('Buyers: ', buyers)
# print('Prices: ', prices)

import urllib.request
from bs4 import BeautifulSoup
import re

url = "https://en.wikipedia.org/wiki/Ubud"
page = urllib.request.urlopen(url) # conntect to website

# try:
#     page = urllib.request.urlopen(url) # conntect to website
# except:
#     print("An error occured with request, check the url.")

soup = BeautifulSoup(page, 'html.parser')
# print(soup)

regex = re.compile('^tocsection-')
content_lis = soup.find_all('li', attrs={'class': regex})
print(content_lis)

content = []
for li in content_lis:
    content.append(li.getText().split('\n')[0])
print(content)