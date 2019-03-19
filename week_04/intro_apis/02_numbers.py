'''
Write a script that connects to the http://numbersapi.com/ and fetches trivia on all
numbers from 0 through 100.

Store the responses in a new JSON file called numbers.json

BONUS:
* fetch information of all the prime numbers from 1-1000
* cycle through the different endpoints the API provides (trivia, math, date, year)
  in a way that they change in binary chunks, e.g.:
  - the info on the first 2 numbers are of type trivia
  - info on the next 4 numbers are of type math
  - the next 8 are on dates
  - etc. (cycle back to the trivia after year)

'''

import requests
import time
import math
import json

type = ["trivia","math", "date", "year"]
data = {}
for i in range(0, 101):
    url = f"http://numbersapi.com/{i}/{type[0]}"
    trivia_n=requests.get(url).text
    data[trivia_n.split()[0]]= trivia_n[-(len(trivia_n) - len(trivia_n.split()[0]) - 1):]
with open("number.json", "a") as f:
    f.write(json.dumps(data))


def prime(l, u):
    '''
       returning the prime numbers from the given lower and upper bounds
    :param l: starting number
    :param u: ending number
    :return: list of prime numbers in the range()
    '''

    l = int(l)
    u = int(u)
    prime = []
    if l > u:
        print("please re-enter the number: lower bound and then upper bound.")
    for i in range(l, u+1):
        count = 0
        for j in range(l+1, i):
            if i % j == 0:
                count += 1
                break
        if count == 0:
            prime.append(i)
    return prime


def prime_binary(start, end):
    '''

    :param start:  starting number (lower bound)
    :param end: ending number (upper bound)
    :return: saved Json file of prime numbers and info in binary chunk manner
    '''
    # tested 10, 100, 1000, 5000
    # end = 1000
    # start = 1
    if end <= start:
        print("please make sure the starting number is smaller than the end number.")
        exit()

    prime_num = prime(start, end)
    if len(prime_num) == 0:
        print("There is no prime number in your range.")
        exit()

    # S(n) = 2^1 + 2^2 + ... 2^n
    # S(n)= 2(2^n-1) = 1000
    x = 0
    pos = []
    start = prime_num[0]
    end = prime_num[-1]
    num = len(prime_num)
    power = math.floor(math.log2(num))
    # find out the position of the chunks to be passed
    for n in range(power):
        x += 2**n
        pos.append(x-1)
    #print(num, pos, power)
    # fill the new type list that matches with the number of chunks
    if math.floor(power/len(type)) == 0:
        type_all = []
    else:
        type_all = type * math.floor(power/len(type))

    for i in range(power%len(type)):
        type_all.append(type[i])
    #print(type_all)

    data = {}
    for i in range(power):
        if i == power - 1:
            x = num
        else:
            x = pos[i+1]
        for j in range(pos[i], x):
            # print(prime_num[j], end="")
            # print(type_all[i], end="")
            # print("\n")
            url = f"http://numbersapi.com/{prime_num[j]}/{type_all[i]}"
            p = requests.get(url).text
            data[p.split()[0]] = p[-(len(p) - len(p.split()[0]) - 1):]

    with open("prime_number.json", "a") as f:
        f.write(json.dumps(data))

prime_binary(1, 1000)