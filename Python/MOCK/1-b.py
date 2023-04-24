class Adder1:
    def add(self, a, b):
        return a + b


class Adder2:
    def add(self, a, b):
        return a + b


class MultiAdder(Adder1, Adder2):
    def sum(self, a, b):
        return self.add(a, b)


adder = MultiAdder()
result = adder.sum(2, 3)
print(result)
