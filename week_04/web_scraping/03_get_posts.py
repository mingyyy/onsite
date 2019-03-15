'''
Create an account at freecycle or use the following:
user: martin-martin
pwd:  bali2019

Using python's request_html library:
* log in to the website
* navigate to the site that contains all posts for the Denver, CO group
* retrieve all post titles from the first page
* save the titles to a file called 'denver_posts.txt'

BONUS: use pagination features to retrieve all posts of all pages in the group
       and save them to the file denver_all.txt

'''
from requests_html import HTMLSession
from requests_html import HTML
import re


url_login = "https://my.freecycle.org/login"
url_home = "https://my.freecycle.org/home/groups"
session = HTMLSession()
#
# # login the website
# payload = {'username': 'martin-martin', 'pass': 'bali2019'}
# p = session.post(url_login, data=payload)
# x = session.get(url_home)
# print("ok" if x.status_code == 200 else "check your code")
#
# # exporting html file after logging in
# with open('free_cycle.html', 'w') as f:
#     f.write(x.text)
# # search for the Denver link
# for link in [i for i in x.html.absolute_links if i[-8:] == "DenverCO"]:
#     print(link)
# # navigate to the DenverCO link and create denver.html file
# d = session.get(link)

# with open('denver.html', 'w') as f:
#     f.write(d.text)

# # find the group post table and export to another html file called denver_post
# p = d.html.find(selector='#group_posts_table', first=True)
# with open('denver_post.html', 'w') as f:
#     f.write(p.text)

# # Retrieve all the titles based on (#\d)
# with open('denver_post.html', 'r') as f:
#     lines = f.readlines()
#
# flag = 0
# post = []
# for line in lines:
#     if flag == 1:
#         post.append(line.split('by')[0])
#         flag = 0
#     if re.match(r'^\(\#', line):
#         flag = 1

# # Write all titles only to file denver_post.txt
# with open('denver_post.txt', 'a') as f:
#     for i in post:
#         f.write(f"{i}\n")


# looking for links of the next pages
# while d.html.next:
#     html = d.html.next() # TODO why _next is none?
#     d = session.get(html)
#     with open('denver.html', 'a') as f:
#         f.write(d.text)
#         p = d.html.find(selector='#group_posts_table', first=True)
#         with open('denver_post.html', 'a') as f:
#             f.write(p.text)

with open("denver.html", "r") as f:
    denver = f.read()
    source = HTML(html=denver)
match = source.find("p")
for i in range(len(match)):
    if match[i].text.startswith("Showing"):
        next_links = match[i].find('a')
        for link in next_links:
            print(link.text)
            nextp = session.get(link.absolute_links)
            nextp.html.find(selector='#group_posts_table', first=True)
            with open('denver_all.txt', 'a') as f:
                f.write(nextp.text)

