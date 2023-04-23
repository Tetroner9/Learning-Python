class Car:
    # Class variable
    wheels = 4

    def __init__(self, make, model, year):
        # Instance variables
        self.make = make
        self.model = model
        self.year = year


car1 = Car("Honda", "Civic", 2022)
car2 = Car("Toyota", "Corolla", 2021)

print(car1.make)
print(car2.year)
