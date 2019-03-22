'''
Following the same process and tools we used in class,
create an API that serves numerical information.

What topic your API is about is your own choice,
however it needs to fulfill the following specs:
* ingest API data from at least 1 external source
* combine (and/or manipulate) the received data in a meaningful way
* store your altered data in a Postgres database
* serve the data at an endpoint (e.g. using sandman2)

TIP: consider using a cryptocurrency API such as coinmarketcap (but anything goes)!

'''
from requests_html import HTMLSession
from pprint import pprint
import sqlalchemy as db
import json

username = "Ming"
password = ""
db_name = "wb"

file_path = '/Users/Ming/Documents/CodingNomads/python-onsite/week_05/mini_projects/wb_country_code.json'

# 2. Create a new DB
# DATABASE_URI = f"postgres+psycopg2://{username}@localhost:5432/"
# engine = db.create_engine(DATABASE_URI, echo=True)
# conn = engine.connect()
# conn.execute("commit")
# conn.execute("create database " + db_name)

DATABASE_URI = f"postgres+psycopg2://{username}@localhost:5432/{db_name}"
engine = db.create_engine(DATABASE_URI, echo=True)
conn = engine.connect()
metadata = db.MetaData()

# 4. load data from wb.country_code.json, then insert into table
# with open(file_path, 'r') as f:
#     file = json.load(f)
#
# ts = db.Table('country_code', metadata, autoload=True, autoload_with=engine)
# query = db.insert(ts)
# result_proxy = conn.execute(query, file)

# 1. world bank api - country code
# cl = []
# counter = 1
# for page_num in range(1, 8):
#     url_Country_Code = f"http://api.worldbank.org/v2/country?page={page_num}&format=json"
#     session = HTMLSession()
#     result_cc=session.get(url_Country_Code)
#     res = result_cc.json()[1]
#
#     # collect country code table: id (string(3)), latitude (double), longitude (double), name (string(30)), region (string(50))
#     for i in res:
#         c = {}
#         for k, v in i.items():
#             if k in ('name', 'id'):
#                 c[k]=v
#             if k in ('latitude', 'longitude'):
#                 if len(v)<=1:
#                     c[k] = 0
#                 else:
#                     c[k] = float(v)
#             if k in ('region', 'incomeLevel'):
#                 c[k] = v["value"]
#         cl.append(c)
#         counter += 1
# # generate json file
# with open('wb_country_code.json','w') as f:
#     json.dump(cl, f, sort_keys=True, indent=4, separators=(',', ': '))

# 3. Create table: country_code
# cc = db.Table('country_code', metadata,
#      db.Column('id', db.String(3), primary_key=True),
#      db.Column('name', db.String(50)),
#      db.Column('latitude', db.DECIMAL),
#      db.Column('longitude', db.DECIMAL),
#      db.Column('region', db.String(50)),
#      db.Column('incomeLevel', db.String(50)))
#
# metadata.create_all(engine)

cc = db.Table('pop_total', metadata,
     db.Column('id', db.Integer, primary_key=True, autoincrement = True),
     db.Column('date', db.Integer),
     db.Column('value', db.DECIMAL),
     db.Column('country_id', db.String(2)),
     db.Column('country_name', db.String(100)))
metadata.create_all(engine)