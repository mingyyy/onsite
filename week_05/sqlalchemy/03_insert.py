'''
Insert a new record in the film table.

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

table_name = 'film'
t = sqa.Table(table_name, metadata, autoload=True, autoload_with=engine)
# Print full table metadata
pprint(repr(t))

query = sqa.insert(t).values(film_id=10000, title="coco", description="cartoon",release_year=2017, language_id=1,
rental_duration=3, rental_rate=4.5, length=130, replacement_cost=19.99, rating='PG-13',
last_update='2018-05-26 14:50:58.951', special_features="Trailers, Commentaries")
# ::tsvector

result = connection.execute(query)