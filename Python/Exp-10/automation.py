import sqlite3


def create_database(database_name):
    conn = sqlite3.connect(database_name)
    conn.close()


def create_table(database_name, table_name):
    conn = sqlite3.connect(database_name)
    conn.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    roll_number INTEGER NOT NULL,
                    address TEXT NOT NULL);''')
    conn.close()


def add_student(database_name, table_name, first_name, last_name, roll_number, address):
    conn = sqlite3.connect(database_name)
    conn.execute(f'''INSERT INTO {table_name} (first_name, last_name, roll_number, address)
                    VALUES (?, ?, ?, ?);''', (first_name, last_name, roll_number, address))
    conn.commit()
    conn.close()


def display_students(database_name, table_name):
    conn = sqlite3.connect(database_name)
    students = conn.execute(f"SELECT * FROM {table_name};").fetchall()
    for student in students:
        print(student)
    conn.close()


def main():
    database_name = 'myclass.db'
    table_name = 'students'
    create_database(database_name)
    create_table(database_name, table_name)
    add_student(database_name, table_name, "Om", "Kadam", 37, "Goregaon")
    add_student(database_name, table_name, "Manav", "Ghadi", 29, "Borivali")
    add_student(database_name, table_name, "Devansh", "Mistry", 46, "Kandivali")
    display_students(database_name, table_name)


if __name__ == '__main__':
    main()
