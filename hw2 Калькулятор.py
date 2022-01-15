while True:
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    operator = input("Введите арифметическое действие: ")
    if operator == '+':
        print("Number1 + number 2 = ", num1+num2)
    if operator == '*':
        print("Number1 * number 2 = ", num1*num2)
    if operator == '-':
        print("Number1 - number 2 = ", num1-num2)
    if operator == '/':
        print("Number1 / number 2 = ", num1/num2)
        