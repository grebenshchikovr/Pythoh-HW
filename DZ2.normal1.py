import math

list = [2, -5, 8, 9, -25, 25, 4]
print(f"Исходный список: {list}")
new_list = []
for item in list:
    if item >= 0 and math.sqrt(item).is_integer():
        new_list.append(int(math.sqrt(item)))
    else:
        pass
print(f"Новый список: {new_list}")
