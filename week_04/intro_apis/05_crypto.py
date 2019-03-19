'''
http://docs.nomics.com/
Using the nomics API, repeatedly fetch the price of Bitcoin for a duration of 10 minutes.
Store each value in a dictionary that uses the time of query as a key.

After the script stopped running, determine programmatically at what query time the price
was the highest, and when the lowest.

HINTS:
- request an API key first and remember to include it in your queries
- the /prices endpoint of the nomics API can be used for achieving this task
- remember to use packages from the standard library, e.g. for time keeping and dates

BONUS: Explore the logging package for easier tracking

'''
import nomics
import requests
import urllib.request
import time
import logging



# modified key
api_key = "7c025f04bcb22dac91510b668268191"


# fetch price for BTC, 10mins
url = "https://api.nomics.com/v1/markets/prices?key=" + api_key + "&currency=BTC"
start = time.time()
interval = 0
while interval <= 600: # out of memory
    raw = urllib.request.urlopen(url).read().decode()
    with open("price.txt", "a") as f:
        f.write(raw)
    end = time.time()
    interval = end - start
    time.sleep(10)

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('This is a Warning')

# store value in a dict, key: time of query
quotes = []
dict_all = {}
with open("price.txt", "r") as f:
    lines = f.readlines()
for line in lines:
    di = line[2:][:-3]
    di = di.split("},{")
    for each in di:
        quotes.append(each)

i, j = 0, 0
for q in quotes:
    i += 1
    unit = q.split('","')
    dict_q = {}
    for each in unit:
        last = each.split('":"')
        key, value = last[0], last[1]
        key, value = key.replace('"', ''), value.replace('"', '')
        dict_q[key] = value
    dict_all[i] = dict_q

dict_price = {}
for value in dict_all.values():
    for k, v in value.items():
        dict_price[value['timestamp']]=value['price']

print(dict_price)
low, high= 4000, 0
for k, v in dict_price.items():
    if float(v)  > high:
        high = float(v)
        high_time = k
    elif float(v) < low:
        low = float(v)
        low_time = k

print(low, low_time)
print(high, high_time)

















