'''
Using the tweepy package, build a script that separates twitter handles
into different groups according to the number of their followers.

The classes can be whatever you like (e.g. I used ASCII art birds ;)

CHALLENGE: Also fetch the number of their friends and display the ratio
between followers and friends in an interesting way.

'''
import tweepy
import mi
import json

auth = tweepy.OAuthHandler(mi.tweepy_api_key, mi.tweepy_api_secret_key)
auth.set_access_token(mi.tweepy_access_token, mi.tweepy_token_secret)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
#
# api.create_friendship("@dan_wegmann")

f = api.followers_ids("@dan_wegmann")
dic = {}
try:
    for i in f:
        followers = api.followers_ids(i)
        friends = api.friends_ids(i)
        dic[i] = [len(followers), len(friends)]
except Exception as err:
    print(err) # [{'message': 'Rate limit exceeded', 'code': 88}]

with open("twitter_.json", "a") as f:
    json.dump(dic, f, sort_keys=True, indent=4, separators=(',', ': '))


with open("twitter_.json", "r") as f:
    c = json.load(f)

print("@dan_wegmann has the following followers")
for k, v in c.items():
    if v[0] > 50: # follower
        print(f"User {k} is popular with {v[0]} followers and has a friend/follower ratio of {int(v[1])/int(v[0]):.2f}.")
    else:
        print(f"User {k} is quite with only {v[0]} followers and has a friend/follower ratio of {int(v[1])/int(v[0]):.2f}")


