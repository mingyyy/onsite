'''
Use the countries API https://restcountries.eu/ to fetch information
on your home country and the country you're currently in.

In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the area of the two countries differ?
* Print the native name of both countries, as well as their capitals

'''

import requests
home = "singapore"
now = "indonesia"
url_home = "https://restcountries.eu/rest/v2/name/" + home
url_now = "https://restcountries.eu/rest/v2/name/" + now

h=requests.get(url_home)
n=requests.get(url_now)

x = h.json()
pop_h = x[0]["population"]
y = n.json()
pop_n = y[0]["population"]

if int(pop_n) > int(pop_h):
    print(f"{now.capitalize()} has a larger population.")
else:
    print(f"{h.capitalize()} has a larger population.")

home_value=[]
now_value=[]
key_home=[]
key_now=[]
for k,v in x[0].items():
    key_home.append(k)
    home_value.append(v)
for k,v in y[0].items():
    key_now.append(k)
    now_value.append(v)

print(key_now == key_home)
count = 0
for i in range(len(key_home)):
    if home_value[i]!=now_value:
        count += 1

print(f"There are {count} areas of the two countries differ.")

capital_home = x[0]["capital"]
capital_now = y[0]["capital"]

native_home = x[0]["nativeName"]
native_now = y[0]["nativeName"]

print(f"{home.title()}'s capital is {capital_home} with native name: {native_home}. ")
print(f"{now.title()}'s capital is {capital_now} with native name: {native_now}. ")

print(x)