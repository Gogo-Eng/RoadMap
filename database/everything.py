#!/usr/bin/python3

from sqlalchemy import create_engine, text
import pandas as pd

host = "localhost"
password = "root"
username = "root"
port = 3306
database = "GogoDB"

url = f"mysql+mysqldb://{username}:{password}@{host}:{str(port)}/{database}"

engine = create_engine(url)
connection = engine.connect()

selector = connection.execute(text('SELECT * FROM property'))

everything = selector.fetchall()
for rows in everything:
    print(rows)

#insert_statement = text('INSERT INTO property(name, age) VALUES(:name, :age)')

#sqlquery = pd.read_sql_query(insert_statement, {'name': 'Chair', 'age': 3})
