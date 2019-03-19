'''
Create a slack API token for the codingnomads workspace.

Using the slackclient package, fetch all comments that include links
from the python-resources channel.

Store the links in a JSON file that has the following form:
[
    {
        "link": "the fetched URL",
        "description": "short blurb describing the resource (if available)",
        "date_added": "when was it posted?",
        "read": False  # defaults to False, change to True if you read it
        "rating": 0  # on a scale from 1-10, initially 0
        "comments": [
            "a list of strings",
            "with comments on the resource",
        ]
        "starred": False,  # defaults to False, change to True if you think it's great
    },
    # next link item
]

We will continue to work with this data throughout the week, so make sure to complete it!

'''

from slackclient import SlackClient
from pprint import pprint
from datetime import datetime
import re
from mi import slack_api
import json

token = slack_api #"xoxp-561901429298-573393925543-580989733156-dd957291729e3bee962017383fa6b4be"
slack_args={"general": "CGH9L0EAV","python_resources": "CGUDWETHR"}
sc = SlackClient(token)

# print(sc.api_call("api.test"))
# print(sc.api_call("channels.info", channel=slack_args["python_resources"]))
# print(sc.api_call(
#         "chat.postMessage", channel=slack_args["python_resources"], text="Hello from Python! :tada::tada::tada:",
#         username='pybot', icon_emoji=':robot_face:'))

hist = sc.api_call("channels.history", channel=slack_args["python_resources"])
sms = hist["messages"]

li = []
for i in sms:
    links = {}
    # pprint(i)
    text = i['text']
    try:
        if text.find("<http") >= 0:
            url = re.findall(r'<.*>', text)
            links['link'] = url[0].strip("<>")
            ts = float(i['ts'])  # unix time
            # if you encounter a "year is out of range" error the timestamp may be in milliseconds, try `ts /= 1000` in that case
            time = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            #url = re.findall(r'<.*>', text)
            try:
                desc = i["attachments"][0]
                description = desc["text"]
            except KeyError:
                desc = "No description."

            try:
                star = i['is_starred']
            except KeyError:
                star = False
            try:
                read = i['last_read']
            except KeyError:
                read = False
            try:
                comments = i["latest_reply"]
            except KeyError:
                comments = "No comments."

            links['date_added'] = time
            if read is not False:
                links["read"] = True
            else:
                links["read"] = read
            if star is not False:
                links["starred"] = True
            else:
                links["starred"] = star
            links["rating"] = 0
            if comments != "No comments.":
                links["comments"] = "There are comments."
            else:
                links["comments"] = comments

            if description != "No description.":
                links["description"]= description
            else:
                links["description"] = desc

            li.append(links)
    except IndexError:
        pass

pprint(li)
with open("slack_resources.json", "w") as f:
    json.dump(li, f, sort_keys=True, indent=4, separators=(',', ': '))


