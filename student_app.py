import psycopg2

# Database connection parameters
db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'Udubra124',
    'host': 'localhost',
    'port': '5432',
}

def get_all_students():
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students;')
        students = cursor.fetchall()
        for student in students:
            print(student)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def add_student(first_name, last_name, email, enrollment_date):
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (first_name, last_name, email, enrollment_date) "
            "VALUES (%s, %s, %s, %s);",
            (first_name, last_name, email, enrollment_date),
        )
        conn.commit()
        print("Student added successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def update_student_email(student_id, new_email):
    conn = None
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE students SET email = %s WHERE student_id = %s;",
            (new_email, student_id),
        )
        conn.commit()
        print(f"Email updated for student {student_id}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

def delete_student(student_id):
    conn = None
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
        conn.commit()
        print(f"Student {student_id} deleted")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    # Example usage:
    get_all_students()
    #add_student("Alice", "Johnson", "alice.johnson@example.com", "2023-09-03")
    #update_student_email(4, "new.email@example.com")
    #delete_student(4)
