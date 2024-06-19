import MySQLdb
from datetime import datetime
db = MySQLdb.connect(host= "localhost", user= "root", passwd= "root", database= "data")

users = [("Gogo-Chinda Progress","progressgogochinda@gmail.com"),
         ("Eteng Yemmy", "etengyemmy@gmail.com")]
user_score = [(45, 100),
              (30, 56)]

mycursor =  db.cursor()

Q1 = "CREATE TABLE Users (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), email VARCHAR(50))"
Q2 = "CREATE TABLE Scores (user_id int PRIMARY KEY, FOREIGN KEY(user_id) REFERENCES Users(id), game1 int DEFAULT 0, game2 int DEFAULT 0)"
Q3 = "INSERT INTO Users (name, email) VALUES (%s, %s)"
Q4 = "INSERT INTO Scores (user_Id, game1, game2) VALUES (%s, %s, %s)"
# mycursor.execute(Q1)
# mycursor.execute(Q2)

mycursor.execute("SHOW TABLES")
for y in mycursor:
    print(y)
for x, user in enumerate(users):
    mycursor.execute(Q3, user)
    last_id = mycursor.lastrowid
    mycursor.execute(Q4, (last_id,) + user_score[x])

db.commit()

mycursor.execute("SELECT * FROM Scores")
for i in mycursor:
    print(i)

mycursor.execute("SELECT * FROM Users")
for t in mycursor:
    print(t)