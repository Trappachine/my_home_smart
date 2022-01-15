import random
num = random.randint(1, 100)
while num !=50:
    num = random.randint(1, 100)
    if num > 50:
        for i in range(num):
            print(num)
    elif num < 50:
        for num2 in range(num):
            num2 = random.random()
            print(num2)
    else:
        print('Вам повезло')
