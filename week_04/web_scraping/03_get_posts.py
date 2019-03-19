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
import math


url_login = "https://my.freecycle.org/login"
url_home = "https://my.freecycle.org/home/groups"
session = HTMLSession()
#
# # login the website
payload = {'username': 'martin-martin', 'pass': 'bali2019'}
p = session.post(url_login, data=payload)
x = session.get(url_home)
print("ok" if x.status_code == 200 else "check your code")
#
# # exporting html file after logging in
# with open('free_cycle.html', 'w') as f:
#     f.write(x.text)

# # search for the Denver link
for link in [i for i in x.html.absolute_links if i[-8:] == "DenverCO"]:
    print(link)
# navigate to the DenverCO link and create denver.html file
d = session.get(link)

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

# with open("denver.html", "r") as f:
#     denver = f.read()
#     source = HTML(html=denver)

match = d.html.find("p")
dict_links = {}
max_num = 0
for i in range(len(match)):
    if match[i].text.startswith("Showing"):
        print(match[i].text)
        next_links = match[i].find('a')

        for link in next_links:
            for next in link.absolute_links:
                page_list = re.findall("(\?page=\d)", next)
                page_num = page_list[0][6:]
                dict_links[page_num] = next
                max_num = int(page_num) if int(page_num) >max_num else max_num
        print(dict_links)
                # nextp = session.get(next)
                # p = nextp.html.find(selector='#group_posts_table', first=True)
                #
                # with open('denver_all.txt', 'a') as f:
                #     f.write(p.text)


def grab_posts(link):
    '''
    :param link: link to one of the posts table
    :return: return the posts at the next page
    '''
    d = session.get(link)
    match = d.html.find("p")
    dict_links = {}
    for i in range(len(match)):
        if match[i].text.startswith("Showing"):
            next_links = match[i].find('a')
            counter = 0
            for link in next_links:
                for next in link.absolute_links:
                    counter += 1  # TODO link.absolute_links is a set
                    print(next, type(next))
                    page_num = re.search("page=[0-9]", next)[2]
                    page_num = page_num[5:]
                    dict_links[page_num] = next
                print(dict_links)
