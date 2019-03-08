import random

n = int(input("Введите размер матрицы"))

for _ in range(n):
    row = [random.randint(1, 9) for _ in range(n)]
    row[random.randint(0, n-1)] = 0
    print(row)