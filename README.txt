# Student Database Management System

This is a simple Python application that allows you to interact with a PostgreSQL database to manage student records.

## Prerequisites

- Python 3.6 or higher
- PostgreSQL
- psycopg2 Python library

## Setup

1. Install Python and PostgreSQL on your machine if you haven't already.
2. Install the psycopg2 library using pip:

pip install psycopg2

3. Set up your PostgreSQL database and create a table named 'students' with the appropriate columns (first_name, last_name, email, enrollment_date).

## Running the Application

1. Open the Python file in your preferred text editor.
2. Update the `db_params` dictionary with your PostgreSQL server details.
3. Save the changes.
4. Run the Python file from the command line:

python filename.py

Replace `filename.py` with the name of your Python file.

## Functions

- `get_all_students()`: Fetches all the student records from the 'students' table in the database.
- `add_student(first_name, last_name, email, enrollment_date)`: Adds a new student record to the 'students' table in the database.
- `update_student_email(student_id, new_email)`: Updates the email of a student record in the 'students' table in the database.
- `delete_student(student_id)`: Deletes a student record from the 'students' table in the database.

## Note

Please ensure that you handle your database credentials securely and do not expose them in your code or version control system.

Youtube link: https://youtu.be/rdxxvdM4PUk