class Student:
    def __init__(self):
        self.percentage = None
        self.chemistry_marks = None
        self.cs_marks = None
        self.physics_marks = None
        self.math_marks = None
        self.name = None
        self.roll_no = None
        self.it_marks = None

    def getstudentdetails(self):
        self.name = input("Enter name: ")
        self.roll_no = input("Enter roll no: ")
        self.math_marks = int(input("Enter Math marks: "))
        self.physics_marks = int(input("Enter Physics marks: "))
        self.cs_marks = int(input("Enter C.S marks: "))
        self.it_marks = int(input("Enter I.T marks: "))
        self.chemistry_marks = int(input("Enter Chemistry marks: "))

    def printresult(self):
        self.percentage = int(
            (self.math_marks + self.physics_marks + self.cs_marks + self.it_marks + self.chemistry_marks) / 500 * 100)
        print("Name: ",self.name, "\nRoll No: ", self.roll_no, "\nPercentage:", self.percentage)


s1 = Student()
s1.getstudentdetails()
print("Result: ")

s1.printresult()
