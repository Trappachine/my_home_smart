num1 = {11, 111, 1111, 11111}
num2 = {22, 222, 2222, 22222}
num3 = {33, 333, 3333, 33333}
num4 = {44, 444, 4444, 44444}
num5 = {55, 555, 5555, 55555}
a = int(input('Введите число1: '))
b = int(input('Введите число2: '))
if b == 0:
    print(Error, b = 0)
else:
    if a/b>10:
        num1.add(10)
        print(num1)
        num2.add(10)
        print(num2)
    elif a/b<10:
        print(num1|num2|num3|num4|num5)
    elif a/b==10:
        num1.clear()
        print(num1)
