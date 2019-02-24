n = int(input("Введите порядковый номер числа Фибоначчи"))
a = 0
b = 1
for __ in range(n):
    a, b = b, a + b
print(a)
