'''
Redo the exercises from '04_dvdrental.txt' in the SQL labs using SQLAlchemy .

'''

import sqlalchemy as db
from pprint import pprint
import pandas as pd
from sqlalchemy.orm import sessionmaker

username = "Ming"
password = ""
# create a new blank database with the name "car_dealership"
db_name = "dvdrental"
DATABASE_URI = f"postgres+psycopg2://{username}@localhost:5432/{db_name}"
engine = db.create_engine(DATABASE_URI, echo=True)
conn = engine.connect()
metadata = db.MetaData()

# SELECT *
# FROM actor WHERE first_name='Penelope';

actor = db.Table('actor', metadata, autoload=True, autoload_with=engine)

query=db.select([actor]).where(actor.columns.first_name == 'Julia')
result = conn.execute(query).fetchall()
fp = pd.DataFrame(result)
print(fp)

# SELECT film.film_id, film.title, a.first_name, a.last_name  FROM film_actor as fa  join film
# ON film.film_id = fa.film_id
# join (SELECT actor_id, first_name, last_name
# FROM actor WHERE first_name='Julia') as a ON a.actor_id = fa.actor_id;

film = db.Table('film', metadata, autoload=True, autoload_with=engine)
fa = db.Table('film_actor', metadata, autoload=True, autoload_with=engine)

j = actor.join(fa, fa.columns.actor_id == actor.columns.actor_id).join(film, film.columns.film_id == fa.columns.film_id)
query=db.select([film.columns.film_id, film.columns.title,actor.columns.first_name, actor.columns.last_name]).select_from(j).where(actor.columns.first_name == 'Julia')
result = conn.execute(query).fetchall()
fp = pd.DataFrame(result)
print(fp)


# SELECT first_name, count(last_name) as number_of_first_name
# FROM actor group by first_name order by number_of_first_name desc;

query = db.select([actor.columns.first_name,db.func.count(actor.columns.last_name).label("number_of_first_name")]).\
    group_by(actor.columns.first_name).order_by(db.desc(db.func.count(actor.columns.last_name)))
result = conn.execute(query).fetchall()
fp = pd.DataFrame(result)
print(fp)