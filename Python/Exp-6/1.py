class Number:
    def __init__(self, num):
        self.num = num


class Cube(Number):
    def find_cube(self):
        return self.num ** 3


num = int(input("Enter a number: "))
c = Cube(num)
print(f"The cube of {num} is {c.find_cube()}")
