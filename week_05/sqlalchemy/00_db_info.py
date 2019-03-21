'''

All of the following exercises should be done using sqlalchemy.

Using the dvdrental schema, write the necessary code to print information about the film and category table.

'''

import sqlalchemy as sqa
from pprint import pprint

username = "Ming"
password = ""
db_name = "dvdrental"
# connection string to postgres
DATABASE_URI = f"postgres+psycopg2://{username}@localhost:5432/{db_name}"
engine = sqa.create_engine(DATABASE_URI, echo=True)
connection = engine.connect()
metadata = sqa.MetaData()


def Get_table(table_name):
    t = sqa.Table(table_name, metadata, autoload=True, autoload_with=engine)
    s = sqa.select([t])
    result = connection.execute(s)
    return result
    # for row in result:
    #    print (row)

for row in Get_table("category"): # category/film
    pprint(row)