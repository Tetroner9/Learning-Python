class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age < 0 or age > 120:
            raise ValueError("Invalid age")
        self._age = age

    age = property(get_age, set_age)


person = Person("John", 25)

# Get the age
print(person.age)

# Set the age
person.age = 30
print(person.age)

person.age = -5
