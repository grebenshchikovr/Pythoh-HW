def fib(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a


def fib_from_n2m(n, m):
    fib_row = []
    if m <= n or m < 0 or n < 0:
        return "не правильные границы диапазона"
    for i in range(n, m + 1):
        fib_row.append(fib(i))
    return fib_row


print("Сейчас выведем ряд Фибоначчи с n-элемента до m-элемента.")

n = int(input("Введите n: "))
m = int(input("А теперь m: "))

print(fib_from_n2m(n, m))
