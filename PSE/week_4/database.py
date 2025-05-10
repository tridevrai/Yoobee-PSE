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

# Add one more Table "course" (name, ID and unit columns ) 
# with two functionality insert and search based on course_ID and user name

def create_table_course():
    conn = create_connection() # create a connection to the database
    cursor = conn.cursor() # create a cursor to execute the SQL commands
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, 
            unit INTEGER NOT NULL
            )
    ''')
    conn.commit() # commit the changes to the database
    conn.close() # close the connection to the database to free up resources


def create_table_junction():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses_users_junction (
            course_id INTEGER,
            user_id INTEGER,    
            PRIMARY KEY (course_id, user_id),
            FOREIGN KEY (course_id) REFERENCES courses(id),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    conn.commit() # commit the changes to the database
    conn.close() # close the connection to the database to free up resources