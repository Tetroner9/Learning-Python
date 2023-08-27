"""
DO NOT COPY THIS PART!
There are three methods to create myclass
1. Automation with functions
2. Class Based
3. With Query

Below is made with_query"""

import sqlite3

def create_table():
    conn = sqlite3.connect('myclass.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS students
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    roll_number INTEGER NOT NULL,
                    address TEXT NOT NULL);''')
    conn.close()


def add_student(first_name, last_name, roll_number, address):
    conn = sqlite3.connect('myclass.db')
    conn.execute('''INSERT INTO students (first_name, last_name, roll_number, address)
                    VALUES (?, ?, ?, ?);''', (first_name, last_name, roll_number, address))
    conn.commit()
    conn.close()


def display_students():
    conn = sqlite3.connect('myclass.db')
    students = conn.execute("SELECT * FROM students;").fetchall()
    for student in students:
        print(student)
    conn.close()


create_table()
add_student("Om", "Kadam", 37, "Goregaon")
add_student("Manav", "Ghadi", 29, "Borivali")
add_student("Devansh", "Mistry", 46, "Kandivali")
display_students()
