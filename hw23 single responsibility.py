import random
class generator():
    def __init__(self):
        self.num1 = random.randint(5, 10123)
    def printer(self):
        print(f'Рандомное число: {self.num1}')
copy =  generator()
copy.printer()