import sqlite3

# add the name of the database
connection = sqlite3.connect(".db")

cursor = connection.cursor()
#select from tables
cursor.execute('SELECT question, * FROM testbank')
# Change question to any row in a table or remove in total to print out entire table

questions = cursor.fetchall()

for r in questions:
    #Where do we print out the tables/rows to?
    print(r)

cursor.close()
connection.close()
