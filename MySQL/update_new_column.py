import MySQLdb
from datetime import datetime
db = MySQLdb.connect(host= "localhost", user= "root", passwd= "root", database= "data")
mycursor = db.cursor()

# mycursor.execute("CREATE TABLE Test (name varchar(50), creation_date datetime, gender ENUM('M', 'F', 'O'), id int PRIMARY KEY NOT NULL AUTO_INCREMENT)") # ENUM allows you to select either male female or other
# mycursor.execute("INSERT INTO Test (name, creation_date, gender) VALUES (%s,%s,%s)", ("Progress", datetime.now(), "M"))

# db.commit()
# mycursor.execute("DESCRIBE Person")
# for x in mycursor:
#     print(x)
# mycursor.execute("SELECT * FROM Person")
# for x in mycursor:
#     print(x)
#mycursor.execute("ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL")
mycursor.execute("UPDATE Test SET food = %s WHERE id = %s", ("Rice", 5))
mycursor.execute("DELETE FROM Test WHERE id IN (8, 7)")
db.commit()
mycursor.execute("SELECT * FROM Test ORDER BY id DESC")
for x in mycursor:
    print(x)