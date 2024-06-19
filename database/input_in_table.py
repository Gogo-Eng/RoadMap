#!/usr/bin/python3

from sqlalchemy import create_engine, text


username = 'root'
password = 'root'
database = 'GogoDB'

url = f"mysql+mysqldb://{username}:{password}@localhost/{database}"

engine = create_engine(url)
connection = engine.connect()

insert_statement = text("INSERT INTO property(name, age) VALUES(:name, :age)")
#The parameters should be passed as a tuple separately from the SQL statement
insert_into_table = connection.execute(insert_statement, [{"name": "Table", "age": 3}, {"name": "Bookshelf", "age": 5}])
connection.commit()
connection.close()