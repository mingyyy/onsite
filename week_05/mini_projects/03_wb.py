from requests_html import HTMLSession
from pprint import pprint
import sqlalchemy as db
import json

username = "Ming"
password = ""
db_name = "wb"

file_path = '/Users/Ming/Documents/CodingNomads/python-onsite/week_05/mini_projects/wb_pop_total.json'

DATABASE_URI = f"postgres+psycopg2://{username}@localhost:5432/{db_name}"
engine = db.create_engine(DATABASE_URI, echo=True)
conn = engine.connect()
metadata = db.MetaData()

# 1. world bank api - country code
# cl = []
# counter = 1
# for page_num in range(1, 60): # 59 pages
#     url_Country_Code = f"http://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?date=2008:2018&page={page_num}&format=json"
#     session = HTMLSession()
#     result_cc = session.get(url_Country_Code)
#     try:
#         res = result_cc.json()[1]
#     except KeyError:
#         print(page_num)
#         pass
#
#     # collect population total
#     for i in res:
#         c = {}
#         for k, v in i.items():
#             if k == "date":
#                 c[k] = int(v)
#             if k == "value":
#                 if v == "None":
#                     c[k] = 0
#                 else:
#                     c[k] = v
#             if k == 'country':
#                 c["country_id"] = v["id"]
#                 c["country_name"] = v["value"]
#         cl.append(c)
#         counter += 1
# # generate json file
# with open('wb_pop_total.json','w') as f:
#     json.dump(cl, f, sort_keys=True, indent=4, separators=(',', ': '))
# print(counter)


# 4. load data from wb.country_code.json, then insert into table
with open(file_path, 'r') as f:
    file = json.load(f)

ts = db.Table('pop_total', metadata, autoload=True, autoload_with=engine)
query = db.insert(ts)
result_proxy = conn.execute(query, file)