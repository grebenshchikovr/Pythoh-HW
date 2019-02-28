import random

list = []
for i in range(10):
    list.append(random.randint(-100, 100))
print(f"Исходный список: {list}")

new_list = []
for item in list:
    if item % 2:
        new_list.append(item * 2)
    else:
        new_list.append(item / 4)
print(f"Новый список: {new_list}")
