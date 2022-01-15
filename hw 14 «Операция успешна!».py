##while True:
##    a = input('Введите число: ')
##    b = input('Введите второе число: ')
##    if a==0 or type(a)==str or b==0 or type(b)==str:
##        print('Error')
##    elif type(a) == int and type(b) == int:
##        print('«Операция успешна!»')
while True:
  try:
    A = float(input('Введите число A: '))
    if A == 0 :
      print('Ошибка!')
      continue
    B = float(input('Введите число B: '))
    print('«Операция успешна!»')
  except ValueError:
    print('Ошибка! Вы не ввели число!')
