age=int(input("Введите возраст: "))
class age:
    def __init__(self):
        self.age=age
    def sw(self):
        if self.age <= 18:
            print("Вы школьник!")
        elif self.age <= 40:
            print("Вы мужчина!")
        elif self.age > 40:
            print("Вы дед!")
copy=age()
copy.sw()