'''
Update all films in the film table to a rental_duration value of 10,
in the length of the movie is more than 150.

'''
import sqlalchemy as db
from pprint import pprint

username = "Ming"
password = ""
db_name = "dvdrental"
# connection string to postgres
DATABASE_URI = f"postgres+psycopg2://{username}@localhost:5432/{db_name}"
engine = db.create_engine(DATABASE_URI, echo=True)
conn = engine.connect()
metadata = db.MetaData()

table_name = 'film'
t = db.Table(table_name, metadata, autoload=True, autoload_with=engine)

# UPDATE film SET rental_duration = 10 WHERE length = 100;
# in total 12 records and rental_duration from 3-6
query = db.update(t).values(rental_duration=10).where(t.columns.length == 100)
result = conn.execute(query)