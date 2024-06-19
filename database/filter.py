#!/usr/bin/python3

from sqlalchemy import create_engine, text, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

# Classes mapped using the Declarative system are defined 
# in terms of a base class (declarative base class)

username = "root"
password = "root"
host = "localhost"
port = 3306
database = "GogoDB"

url = f"mysql+mysqldb://{username}:{password}@{host}:{str(port)}/{database}"
engine = create_engine(url)
conection = engine.connect()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    fullname = Column(String(50))
    email = Column(String(50))

    def __repr__(self):
        return f"[{self.fullname}]:[{self.email}] >> {self.id}"

# Create all tables defined by Base subclasses on the database
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session= Session()

# session.query(User): This initiates a query on the User table.
# filter(User.name.in_([Gogo-Chinda Progress", "Yemmy"])): This adds a filter condition to the 
# query, specifying that the name attribute of User should be in the list [Gogo-Chinda Progress", "Yemmy"].
# .all(): This method executes the query and returns all results as a list of User objects.
result = session.query(User).filter(User.fullname.in_(["Gogo-Chinda Progress", "Yemmy"])).all()
for user in result:
    print(user.fullname)

session.close()
