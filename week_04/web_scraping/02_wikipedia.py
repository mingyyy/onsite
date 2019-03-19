'''
Using requests_html scrape information from a wikipedia page that interests you.
( you can use: https://en.wikipedia.org/wiki/Ubud )

Collect:
* all the information recorded in the infobox on the right
* 2 links to images on the site
* an interesting fact or quote from the page
* a collection of all the resources (titles and links) related to the page

Store the information in a nicely formatted text file.

'''
from requests_html import HTMLSession

url="https://en.wikipedia.org/wiki/Rumi"
session = HTMLSession()
page = session.get(url)

# infobox
info = page.html.find('#mw-content-text > div > table', first=True)
print(info.text)

# links of images
images=page.html.find('img')
for i in images:
    for j in i.html.split():
        if j[-3:] =="png":
            try:
                print(j.split('="')[1])
            except IndexError:
                pass


# collecting all links & titles related to the page
link = [x for x in page.html.absolute_links]
titles = page.html.find(selector= '#toc', first = True)
print(titles.text)
print(titles.link)


# an interesting fact or quote from the page
quotes = page.html.find(".templatequote")
for q in quotes:
    print(q.text + "\n")


'''
# url = "https://en.wikipedia.org/wiki/Sorting_algorithm"
# session = HTMLSession()
# page = session.get(url)
#
#
# # infobox
#
# # an interesting fact related to "shuffling"
# others = page.html.find('a', containing = 'shuffle')
# for x in others:
#     print(x)


# collecting all links related to the page
# link = [x for x in page.html.links]
# link = [x for x in page.html.absolute_links]

# collecting all titles related to the page
# titles = page.html.find(selector= '#toc', first = True)
# print(titles.text)

# finding links to photos on this page
# link = [x for x in page.html.links if x[-3:] == "svg"]
# for x in link:
#     print()
#     print(x)
'''



