while True:
    num1 = input("Введите число 1: ")
    num2 = input("Введите число 2: ")
    if num1.isdigit() and num2.isdigit():
        num3 = int(num1) + int(num2)
        print("Сумма чисел:", num3)
    else:
        print("Вы ввели не число")
