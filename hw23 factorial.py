num1= int(input('Число:'))
first = 1
for i in range(1, num1+1):
    first = i*first
    print(first)
############################################################################
import math
num2 = int(input('Число2:'))
print(math.factorial(num2))