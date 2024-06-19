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
insert_in_table = Session()

new_user = User(fullname="Chinda Pearl", email="pearlchinda@gmail.com")
insert_in_table.add(new_user)
#insert_in_table.add_all([User(fullname="Gogo-Chinda Wisdom", email="wisdomgogochinda@gmail.com"),
#                         User(fullname="Eteng Yemmy", email="etengyemmy@gmail.com")])
insert_in_table.commit()

for instance in insert_in_table.dirty: # nothing will print, because the changes was commited
    print(instance)



