x = int(input("Введите целое число"))
a = 0
for i in range(2, x):
    if x % i:
        pass
    else:
        a += 1
if a == 0:
    print("Число", x, "простое")
else:
    print("Число", x, "не простое")
