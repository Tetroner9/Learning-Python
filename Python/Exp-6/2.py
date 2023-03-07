class Shape:
    def __init__(self, shape_name):
        self.shape_name = shape_name

    def get_name(self):
        return self.shape_name


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height


# create objects of Rectangle, Circle and Triangle class and call their get_area() methods
rect = Rectangle(5, 10)
print(f"The area of {rect.get_name()} is {rect.get_area()}")

circle = Circle(7)
print(f"The area of {circle.get_name()} is {circle.get_area()}")

tri = Triangle(4, 6)
print(f"The area of {tri.get_name()} is {tri.get_area()}")
