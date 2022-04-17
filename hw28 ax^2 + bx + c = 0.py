import math
def core():
    print('ax**2+bx+c=0')
    a = int(input('Введите а: '))
    b = int(input('Введите b: '))
    c = int(input('Введите c: '))
    D = b**2 - 4*a*c
    if D>0:
        cor_D = math.sqrt(D)
        print(f"{D} - дискриминант, {cor_D} - корень дискриминанта")
        x1 = int(-b + cor_D) / (2*a)
        x2 = int(-b - cor_D) / (2*a)
        print(f'Корни уравнения: {x1}, {x2}')
    elif D==0:
         print(f"{D} - дискриминант")
         x1 = -b / (2*a)
         print(f'Корень уравнения: {x1}')
    else:
        print('Невозможно')
core()