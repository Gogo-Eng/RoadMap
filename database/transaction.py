from sqlalchemy import create_engine, text
import pandas as pd

# Database credentials
username = 'root'
password = 'root'
database = 'GogoDB'
url = f"mysql+mysqldb://{username}:{password}@localhost/{database}"

# Create the SQLAlchemy engine
engine = create_engine(url)

# Insert data into the table and commit changes
with engine.connect() as connection:
    with connection.begin() as transaction:
        try:
            # Execute the insert query
            connection.execute(text("INSERT INTO property(name, age) VALUES(:name, :age)"), {"name": "Standing fan", "age": 6})
            # Commit the transaction
            transaction.commit()
        except:
            # Rollback the transaction in case of error
            transaction.rollback()
            raise

# Fetch data using pandas
df = pd.read_sql("SELECT * FROM property", engine)
print(df)
