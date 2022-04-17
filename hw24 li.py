print('Генерация чисел с дальнейшим переможением, суммой')
class numb():
    def __init__(self):
        self.num1 = int(input('Введите 1 число: '))
        self.num2 = int(input('Введите 2 число: '))
    def sum(self):
        print('num3 = ', self.num1+self.num2)
    def umn(self):
        print('num3 = ', self.num1*self.num2)
copy = numb()
copy.sum()
copy.umn()