def second_lowest_marks(students):
    student_list = [(name, marks) for name, marks in students]
    student_list.sort(key=lambda x: x[1])
    second_lowest = sorted(list(set([marks for name, marks in student_list])))[1]
    second_lowest_students = sorted([name for name, marks in student_list if marks == second_lowest])
    return second_lowest_students


n = int(input("Enter the number of students: "))
students = []
for i in range(n):
    name = input("Enter the name of student: ")
    marks = int(input("Enter the marks of student: "))
    students.append((name, marks))

second_lowest_students = second_lowest_marks(students)

print("The students with the second lowest marks:")
for student in second_lowest_students:
    print(student)
