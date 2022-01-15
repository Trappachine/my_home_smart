import datetime
from datetime import date
y = int(input('пользователь вводит свой возраст: '))
z = int(input('Номер месяца рождения: '))
x = int(input('День рождения: '))
b = 2022-y
a = datetime.date(b, z, x)
print(a)
