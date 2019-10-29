def create_connection(db_file):
    ### create a database connection to the SQLite database

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn
# This function selects all rows from the tasks table and display the data:

def select_all_tasks(conn):

    cur = conn.cursor()
    #Choose Table /rows
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    for row in rows:
        print(row)
        #The line above just prints out the rows in the databse table, where should we print them?
