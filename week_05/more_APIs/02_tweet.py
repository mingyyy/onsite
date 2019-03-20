'''
Using tweepy, create a script that programmatically tweets to your twitter account.

Create a JSON file that includes a number of tweets you want to post.
Your script should read from that JSON file, select some text and tweet it
whenever you run the script.

BONUS: Look into CRON jobs to automate your tweets to go out at scheduled times.
       E.g.: "Don't start without me, I'm nearly there!" every weekday at 9:14... ;P

'''

import tweepy
import json
import mi
from random import randint

auth = tweepy.OAuthHandler(mi.tweepy_api_key, mi.tweepy_api_secret_key)
auth.set_access_token(mi.tweepy_access_token, mi.tweepy_token_secret)

api = tweepy.API(auth)

with open("/Users/Ming/Documents/CodingNomads/python-onsite/week_05/more_APIs/tweets_generator.json", "r") as f:
    c = json.load(f)
for k in c:
    if str(k) == str(randint(1,5)):
        tweet = c[k]
api.update_status(tweet)

# # create the json file
# tfile={}
# tfile[1]="Hello, Daniel! :D from pybot"
# tfile[2]="Hei, Mr. Martin! :D from pybot"
# tfile[3]="Hola, Mr. Cade! :D from pybot"
# tfile[4]="Hola, Sabine! :D from pybot"
# tfile[5]="Hi, Melissa! :D from pybot"
#
# with open("tweets_generator.json", "w") as f:
#     json.dump(tfile, f, sort_keys=True, indent=4, separators=(',', ': '))


# # sending direct sms doesn't work
# event = {
#   "event": {
#     "type": "message_create",
#     "message_create": {
#       "target": {
#         "recipient_id": '3044126985'
#       },
#       "message_data": {
#         "text": 'Hola, como esta?'
#       }
#     }
#   }
# }
# api.send_direct_message(event)