num_students = int(input("Enter the number of students: "))

# create a list to hold student names and grades
students = []

# get input for student names and grades
for i in range(num_students):
    name = input(f"Enter the name of student {i+1}: ")
    marks = [int(x) for x in input(f"Enter the marks for {name} (separated by spaces): ").split()]
    total_marks = sum(marks)
    students.append((name, total_marks))

# sort the list of students by total marks
students.sort(key=lambda x: x[1])

# find the second-lowest total marks
second_lowest_marks = 0
for i in range(num_students):
    if students[i][1] > students[0][1]:
        second_lowest_marks = students[i][1]
        break

# print the names of students with the second-lowest marks
print("Students with the second lowest marks:")
for student in students:
    if student[1] == second_lowest_marks:
        print(student[0])
