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


selector = pd.read_sql_query('SELECT * FROM property', engine)
print(selector)
