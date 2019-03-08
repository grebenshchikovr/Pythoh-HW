import re

with open("pwd.txt", "r") as f:
    list = f.read()

password_list = re.findall(';([\s\S]+?)\n', list)

stat = {}

for i in password_list:
    if i not in stat:
        stat[i] = 1
    else:
        stat[i] += 1

print("Топ-10 паролей в файле:")
for i in range(10):

    max_value = max(stat.values())  # maximum value
    for key, value in stat.items():
        if value == max_value:
            print(f"{i+1}. {key} используется {stat.pop(key)} раз")
            break