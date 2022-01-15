import random
lst = [5, 8, 1, 6, 0]
num1 = random.randint(0,10)
num2 = random.randint(0,10)
print('num2:', num2)
print('num1:', num1)
if num1 > num2:
    lst.append(num1)
    print('New list: ', lst)
elif num1 < num2:
    for lotnum in range(10):
        lotnum = random.randint(-20, 20)
        print('Рандомные числа: ', lotnum)
else:
     print('num1=num2')
