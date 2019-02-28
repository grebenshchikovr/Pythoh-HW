list1 = [1, 2, 3, 4, 5, 6]
print(f'Первый список:{list1}')
list2 = [4, 5, 6, 7, 8, 9, 0]
print(f'Второй список:{list2}')
for item in list2:
    if item in list1:
        list1.remove(item)
print(f'Удаляем из певрого списка втрой: {list1}')
