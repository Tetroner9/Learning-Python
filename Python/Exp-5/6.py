class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0 or age > 120:
            raise ValueError("Invalid age")
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


person = Person("John", 25)

# Get the name and age
print(person.name)
print(person.age)

# Set the name and age
person.name = "Bob"
person.age = 30

# Get the updated name and age
print(person.name)
print(person.age)

# Try to set an invalid age
try:
    person.age = -5
except ValueError as e:
    print(e)
