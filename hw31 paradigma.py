class Engine:
    def engine_method(self):
        print("Это родительский метод из класса engine")
class Car(Engine):
    def car_method(self):
        print("Это метод наследник")
c=Car()
c.engine_method()
c.car_method()
############################################
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        def info(self):
            print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")
        def make_sound(self):
            print("Meow")
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")
    def make_sound(self):
        print("Bark")
cat1 = Cat("Kitty", 25)
dog1 = Dog("Fluffy", 4)
for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
###########################################

