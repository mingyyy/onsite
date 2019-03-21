'''
Redo the exercises from '03_pgadmin.txt' in the SQL labs using SQLAlchemy .

'''
import sqlalchemy as db
from pprint import pprint
import pandas as pd
from sqlalchemy.orm import sessionmaker

username = "Ming"
password = ""
# create a new blank database with the name "car_dealership"
db_name = "car_dealership"
DATABASE_URI = f"postgres+psycopg2://{username}@localhost:5432/{db_name}"
engine = db.create_engine(DATABASE_URI, echo=True)
conn = engine.connect()
metadata = db.MetaData()

# to truncate the Table: users
# Session = sessionmaker(bind=engine)
# session = Session()
# session.execute('''TRUNCATE TABLE users_cars''')
# session.commit()
# session.close()


# - create a new table named "users_cars" with the following fields:
#     - id (auto increment)
#     - user_id (refers to "id" in users table)
#     - car_id (refers to "id" in cars table)
uc = db.Table('users_cars', metadata,
              db.Column('id', db.Integer(), autoincrement=True, primary_key=True),
              db.Column('user_id', db.Integer(), nullable=False),
              db.Column('car_id', db.Integer(), nullable=False)
              )

# - create a new table named "users" with the following fields
#     - id (auto increment)
#     - first name
#     - last name
u = db.Table('users', metadata,
              db.Column('id', db.Integer(), autoincrement=True, primary_key=True),
              db.Column('first_name', db.String()),
              db.Column('last_name', db.String())
              )

# - create a new table named "cars" with the following fields
#     - id (auto increment)
#     - make
#     - model
#     - color
#     - year
c = db.Table('cars', metadata,
              db.Column('id', db.Integer(), autoincrement=True, primary_key=True),
              db.Column('make', db.String(30)),
              db.Column('model', db.String(30)),
              db.Column('color', db.String(20)),
              db.Column('year', db.Integer())
              )

metadata.create_all(c, u, uc)

# Insert into the tables, five records each
# records=[
#     {'id': 100, 'first_name': 'Martin', 'last_name': 'Martin'},
#     {'id': 101,'first_name': 'Michael', 'last_name': 'Jordan'},
#     {'id': 102,'first_name': 'Caden', 'last_name': 'Bikram'},
#     {'id': 103,'first_name': 'Blake', 'last_name': 'Beyond'},
#     {'id': 104,'first_name': 'Freddy', 'last_name': 'Cacoon'}
# ]
# query = u.insert()
# result_proxy = conn.execute(query, records)

# records=[
#     {'id': 1, 'make': 'Toyota', 'model': 'Land Cruiser', 'color':'red', 'year':2008},
#     {'id': 2, 'make': 'Tesla', 'model': 'S5', 'color':'white', 'year':2018},
#     {'id': 3, 'make': 'BMW', 'model': 'Explorer', 'color':'orange', 'year':2004},
#     {'id': 4, 'make': 'KIA', 'model': 'Pathfinder', 'color':'silver', 'year':1997},
#     {'id': 5, 'make': 'Benz', 'model': 'Super', 'color':'black', 'year':2000}
# ]
# query = c.insert()
# result_proxy = conn.execute(query, records)

# records=[
# #     {'id': 1001, 'user_id': 100, 'car_id': 3},
# #     {'id': 1002, 'user_id': 101, 'car_id': 5},
# #     {'id': 1003, 'user_id': 102, 'car_id': 1},
# #     {'id': 1004, 'user_id': 103, 'car_id': 4},
# #     {'id': 1005, 'user_id': 104, 'car_id': 2}
# # ]
# # query = uc.insert()
# # result_proxy = conn.execute(query, records)

#     - select all records from users
#     SELECT * FROM users;
# query = db.select([u])
# result = conn.execute(query).fetchall()
# df = pd.DataFrame(result)
# print(df)

#     - select all records from cars where car make = "Toyota"
#     SELECT * FROM cars WHERE make = 'Toyota';
# query = db.select([c]).where(c.columns.color == 'red')
# result = conn.execute(query).fetchall()
# df = pd.DataFrame(result)
# print(df)

#     - use a join to select the first name and car model of every user who has bought a car
#    SELECT users.first_name, cars.model FROM users_cars AS uc JOIN cars ON uc.car_id = cars.id
#    JOIN users ON users.id = uc.user_id;

# j = uc.join(u, uc.columns.user_id == u.columns.id).join(c, c.columns.id == uc.columns.car_id)
# query = db.select([c.columns.model, u.columns.first_name]).select_from(j)
# result = conn.execute(query).fetchall()
# df = pd.DataFrame(result)
# print(df)

#     - use a join to select the first and last name of everyone who has bought a red car
#     SELECT users.first_name, users.last_name FROM users_cars AS uc JOIN cars ON uc.car_id = cars.id
#    JOIN users ON users.id = uc.user_id WHERE cars.color = 'red';

# j = uc.join(u, uc.columns.user_id == u.columns.id).join(c, c.columns.id == uc.columns.car_id)
# query = db.select([u.columns.first_name, u.columns.last_name]).select_from(j).where(c.columns.color == 'red')
# result = conn.execute(query).fetchall()
# df = pd.DataFrame(result)
# print(df)

#     - use an insert statement to create a new record in each table.
#     INSERT INTO public.users (id, first_name, last_name)
#     VALUES (105, 'Sarah', 'Parking')

# query = db.insert(u).values(id=105, first_name='Sarah', last_name='Parking')
# result = conn.execute(query)


#     INSERT INTO public.cars (id, make, model, color, year)
#     VALUES (6, 'Toyota', 'camery', 'lime', 2003)

# query = db.insert(c).values(id=6, make='Toyota', model='camery', color='lime', year=2003)
# result = conn.execute(query)


#     INSERT INTO public.users_cars (id, user_id, car_id)
#     VALUES (10, 7, 9)

# query = db.insert(uc).values(id=1006, user_id=105, car_id=6)
# result = conn.execute(query)


#     - use sql to update a record in the "cars" table
#     UPDATE cars SET color = 'papaya red' WHERE id = 5;

# query = db.update(c).values(color='papaya red').where(c.columns.id == 6)
# result = conn.execute(query)

#     - delete one record from the database
#    DELETE FROM users_cars WHERE id = 7;

# query = db.delete(c).where(c.columns.id == 6)
# result = conn.execute(query)
