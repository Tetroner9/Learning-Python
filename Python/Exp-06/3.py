class Adder:
    def add(self, x, y):
        return x + y


class Multiplier:
    def multiply(self, x, y):
        return x * y


class Calculator(Adder, Multiplier):
    pass


calc = Calculator()

num1 = 5
num2 = 10

print("Sum:", calc.add(num1, num2))
print("Product:", calc.multiply(num1, num2))
