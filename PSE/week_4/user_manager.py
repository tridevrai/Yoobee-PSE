from database import create_connection
import sqlite3

def add_user(name, email):
    conn = create_connection() # create a connection to the database
    cursor = conn.cursor() # create a cursor to execute the SQL commands
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email)) 
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def view_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall() # fetch all the rows from the database
    conn.close()
    return rows

def search_user(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_user(id,name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ? AND name LIKE ?", (id, '%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")
