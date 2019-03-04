def round(x):
    x = float(x)
    if (x % 1) >= 0.5:
        x = (x // 1) + 1
    else:
        x = x // 1
    return int(x)


x = input("Введите десятичное число для округления: ")
print(round(x))
