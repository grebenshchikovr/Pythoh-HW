import random

list = []
n = int(input("Укажите длину списка, n"))
for __ in range(n):
    item = random.randint(-100, 100)
    list.append(item)
print(list)
