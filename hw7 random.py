import random
a = tuple([random.randint(-1, 5) for _ in range(10)])
b = tuple([random.randint(-5, 1) for _ in range(10)])
c = a + b
print(c, f'Количество нулей: {c.count(0)}', sep='\n')
