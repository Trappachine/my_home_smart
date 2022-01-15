from figure import triangle, circle, square
while True:
    choice = int(input("Выберите: 1 - посчитать площадь треугольника, 2-вычислить длину окружности, 3-вычислить периметр квадрата: "))
    if choice == 1:
        triangle()
    elif choice == 2:
        circle()
    elif choice == 3:
        square()
    else:
        print("нет")
