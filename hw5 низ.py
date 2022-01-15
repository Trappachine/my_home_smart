from time import sleep
test1 = input("Введите текст: ")
lower1 = (test1.lower())
print("Вы ввели:",lower1)
test2 = input("Введите: ")
lower2 = (test2.lower())
print("Конкатенированная строка: ", lower1 + lower2)
sleep(2)
