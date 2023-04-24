class Student:
    def __init__(self):
        self.percentage = None
        self.chemistry_marks = None
        self.cs_marks = None
        self.physics_marks = None
        self.math_marks = None
        self.it_marks = None
        self.name = None
        self.roll_no = None

    def getstudentdetails(self):
        self.name = input("Enter name: ")
        self.roll_no = input("Enter roll no: ")
        self.math_marks = int(input("Enter Math marks: "))
        self.physics_marks = int(input("Enter Physics marks: "))
        self.cs_marks = int(input("Enter C.S marks: "))
        self.it_marks = int(input("Enter I.T marks: "))
        self.chemistry_marks = int(input("Enter Chemistry marks: "))

    def calculate_percentage(self):
        self.percentage = int(
            (self.math_marks + self.physics_marks + self.cs_marks + self.it_marks + self.chemistry_marks) / 500 * 100)

    def calculate_grade(self):
        if self.percentage >= 90:
            return 'A'
        elif self.percentage >= 80:
            return 'B'
        elif self.percentage >= 70:
            return 'C'
        elif self.percentage >= 60:
            return 'D'
        else:
            return 'F'

    def printresult(self):
        self.calculate_percentage()
        grade = self.calculate_grade()
        print("Name: ", self.name, "Percentage: ", self.percentage)


s1 = Student()
s1.getstudentdetails()
print("\nResult:")
s1.printresult()
