class Number:
    def __init__(self, num):
        self.num = num


class Cube(Number):
    def find_cube(self):
        return self.num ** 3


c = Cube(3)
print(c.find_cube())

