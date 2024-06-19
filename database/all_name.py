from sqlalchemy import create_engine, text
import pandas as pd

# Define the database connection details
username = 'root'
password = 'root'
host = 'localhost'
port = 3306
database = 'GogoDB'

# Create the database connection URL
url = f"mysql+mysqldb://{username}:{password}@{host}:{port}/{database}"

# Create the engine and connect to the database
engine = create_engine(url)
connection = engine.connect()

# Define the select statement with a LIKE filter
# select_statement = text("SELECT * FROM users WHERE fullname LIKE :name_pattern")

# Execute the select statement
# result = connection.execute(select_statement, {"name_pattern": '%Progress%'})


selector = pd.read_sql_query("SELECT * FROM users WHERE fullname LIKE '%%Progress%%'", engine)
print(selector)

# Fetch all matching rows
# matching_rows = result.fetchall()

# # Print the matching rows
# for row in matching_rows:
#     print(row)

# Close the connection
connection.close()
