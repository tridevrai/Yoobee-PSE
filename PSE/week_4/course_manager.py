from database import create_connection

def add_course(name, unit, user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO courses (name, unit) VALUES (?, ?)", (name, unit))
    course_id = cursor.lastrowid
    cursor.execute("INSERT INTO courses_users_junction (course_id, user_id) VALUES (?, ?)", (course_id, user_id))
    conn.commit()
    conn.close()

def view_courses():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    rows = cursor.fetchall()
    conn.close()
    return rows

# creating a junction table to link courses and users
def search_course(course_id,user_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
                    SELECT c.id, c.name, c.unit, u.name
                    FROM courses c
                    JOIN courses_users_junction cuj ON c.id = cuj.course_id
                    JOIN users u ON u.id = cuj.user_id
                    WHERE c.id = ? AND u.name = ?
                    '''
        , (course_id, user_name))
    rows = cursor.fetchall()
    conn.close()
    return rows