'''
Sign up for an API key with the new coinmarketcap API.

Using their documentation, fetch all listed cryptocurrencies.
From the result, create a new JSON file that includes the following:
* cmc_rank
* name
* symbol
* platform
* quote

Save that info to a file.
'''

import mi
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '100',
    'convert': 'USD',
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': mi.coinmarketcap_key,
}

session = Session()
session.headers.update(headers)

per_coin={}
all = []
try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    for k, v in data.items():
        for coins in data["data"]:
            for key, value in coins.items():
                per_coin = {}
                per_coin["name"] = coins["name"]
                per_coin["cmc_rank"] = coins["cmc_rank"]
                per_coin["symbol"] = coins["symbol"]
                per_coin["platform"] = coins["platform"]
                per_coin["quote"] = coins["quote"]
            all.append(per_coin)

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


with open("coincap.json","w") as f:
    json.dump(all,f,sort_keys=True, indent=4, separators=(',', ': '))
