'''

Building on the example more_APIs/00_slack, make a new database with two tables to model this object:

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
}

Think about what tables are required to model this object. Do you need two tables? Three?

Now, instead of saving the list of these objects to a JSON file, persist the data
to your database.

NOTE: If you run this several times you will be saving the same information in the table.
To prevent this, you should add a check to see if the record already exists before inserting it.

'''

import sqlalchemy as sqa
from pprint import pprint
import json

username = "Ming"
password = ""
db_name = "test"
# connection string to postgres
DATABASE_URI = f"postgres+psycopg2://{username}@localhost:5432/{db_name}"
# "/mysql://"
file_path = '/Users/Ming/Documents/CodingNomads/python-onsite/week_05/more_APIs/slack_resources.json'

engine = sqa.create_engine(DATABASE_URI, echo=True)
connection = engine.connect()
metadata = sqa.MetaData()

# Create table: slack

# ts = sqa.Table('slack', metadata,
#      sqa.Column('id', sqa.Integer, autoincrement=True, primary_key=True),
#      sqa.Column('comments', sqa.String(1000)),
#      sqa.Column('date_added', sqa.DateTime),
#      sqa.Column('description', sqa.String(1000)),
#      sqa.Column('link', sqa.String(1000), nullable=False),
#      sqa.Column('rating', sqa.Integer),
#      sqa.Column('read', sqa.Boolean),
#      sqa.Column('starred', sqa.Boolean),
#                    )
# metadata.create_all(engine)

# load the file from slack_resources.json
with open(file_path, 'r') as f:
    file = json.load(f)

for post in file:
    pprint(post)

# ts = sqa.Table('slack', metadata, autoload=True, autoload_with=engine)
# query = sqa.insert(ts)
# result_proxy = connection.execute(query, file)
