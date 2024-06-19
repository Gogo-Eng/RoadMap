import MySQLdb
db = MySQLdb.connect(host= "localhost", user= "root", passwd= "root", database= "testdatabase")
mycursor = db.cursor()

mycursor.execute("INSERT INTO Person (name, age) VALUES (%s,%s)", ("Progress", 25))
db.commit()
mycursor.execute("DESCRIBE Person")
for x in mycursor:
    print(x)
mycursor.execute("SELECT * FROM Person")
for x in mycursor:
    print(x)