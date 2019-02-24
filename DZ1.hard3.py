n = int(input("Введите количество строк"))
m = int(input("Введите количество троек ААА"))
aaa = "AAA"
bbb = "BBB"
for i in range(0, n):
    string = (aaa + bbb) * m
    aaa, bbb = bbb, aaa
    print(string)
