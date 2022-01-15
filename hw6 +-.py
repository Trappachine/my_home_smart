numbers = [1, 2, -4, 6, -7, 2]
print("Отрицательных чисел",sum(1 for number in numbers if number < 0))
print("положительных чисел",sum(1 for number in numbers if number > 0))
