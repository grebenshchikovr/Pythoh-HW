import math

x = int(input("Введите целое число"))
x = math.fabs(x)
b = 0
while x > 1:
    a = x % 10
    x = int(x / 10)
    if a > b:
        b = a

print("Наибольшая цифра введенного числа -", b)
