import MySQLdb
from datetime import datetime
db = MySQLdb.connect(host= "localhost", user= "root", passwd= "root", database= "data")
mycursor = db.cursor()

#mycursor.execute("CREATE TABLE Try (name varchar(50), creation_date datetime, gender ENUM('M', 'F', 'O'), id int PRIMARY KEY NOT NULL AUTO_INCREMENT)") # ENUM allows you to select either male female or other
# mycursor.execute("INSERT INTO Test (name, creation_date, gender) VALUES (%s,%s,%s)", ("Blessing", datetime.now(), "F"))
mycursor.execute("USE data")
mycursor.execute("SHOW TABLES")
tables = mycursor.fetchall() 
for table in tables:
    print(table[0])

mycursor.close()
db.close()
# db.commit()
# mycursor.execute("DESCRIBE Person")
# for x in mycursor:
#     print(x)
# mycursor.execute("SELECT * FROM Person")
# for x in mycursor:
#     print(x)