list = [12, 10, 3, 8, 9, -6]

new_list = [value for value in list if value % 4 and not value % 3 and value >= 0]

print(new_list)