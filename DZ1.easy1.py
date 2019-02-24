import math

x = int(input("Введите целое число"))
x = int(math.fabs(x))
while x > 1:
    a = x % 10
    x = int(x / 10)
    print(a)
