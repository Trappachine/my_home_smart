class Calculator:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
    def plus(self):
        return self.num1 + self.num2
    def minus(self):
        return self.num1 - self.num2
    def delt(self):
        return self.num1 / self.num2
    def umn(self):
        return self.num1 * self.num2
 
calc = Calculator(5, 2)
print(calc.plus())
print(calc.minus())
print(calc.delt())
print(calc.umn())
