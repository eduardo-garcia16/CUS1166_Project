import sqlite3

# add the name of the database
connection = sqlite3.connect(".db")

cursor = connection.cursor()
#select from tables
cursor.execute("SELECT  FROM ;")

questions = cursor.fetchall()

for r in questions:
    #print them to..?
    print(r)

cursor.close()
connection.close()
