class Num1:
    def __init__(self):
        self.num1 = None

    def input1(self):
        self.num1 = 10


class Num2:
    def __init__(self):
        self.num2 = None

    def input2(self):
        self.num2 = 2


class Result(Num1, Num2):
    def printresult(self):
        super().input1()
        super().input2()
        print(self.num1 + self.num2)


r = Result()
r.printresult()
