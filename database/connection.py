#!/usr/bin/python3

from sqlalchemy import create_engine, text


username = 'root'
password = 'root'
database = 'GogoDB'

url = f"mysql+mysqldb://{username}:{password}@localhost/{database}"

engine = create_engine(url)
connection = engine.connect()

create_table = connection.execute(text("CREATE TABLE property(name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)"))
connection.close()