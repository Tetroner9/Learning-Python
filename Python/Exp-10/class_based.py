import sqlite3


class MyClassDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('myclass.db')
        self.create_table()

    def __del__(self):
        self.conn.close()

    def create_table(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS students
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        roll_number INTEGER NOT NULL,
                        address TEXT NOT NULL);''')

    def add_student(self, first_name, last_name, roll_number, address):
        self.conn.execute('''INSERT INTO students (first_name, last_name, roll_number, address)
                        VALUES (?, ?, ?, ?);''', (first_name, last_name, roll_number, address))
        self.conn.commit()

    def display_students(self):
        students = self.conn.execute("SELECT * FROM students;").fetchall()
        for student in students:
            print(student)


my_db = MyClassDatabase()
my_db.add_student("Om", "Kadam", 37, "Goregaon")
my_db.add_student("Manav", "Ghadi", 29, "Borivali")
my_db.add_student("Devansh", "Mistry", 46, "Kandivali")
my_db.display_students()
