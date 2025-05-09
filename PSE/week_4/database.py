import sqlite3

def create_connection():
    conn = sqlite3.connect("users.db") # create a connection to the database named users.db
    # if the database does not exist, it will be created
    return conn

def create_table():
    conn = create_connection() # create a connection to the database
    cursor = conn.cursor() # create a cursor to execute the SQL commands
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit() # commit the changes to the database
    conn.close() # close the connection to the database to free up resources
