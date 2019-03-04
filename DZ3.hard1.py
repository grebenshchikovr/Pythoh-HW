import os.path

def is_data():
    """
    Проверка есть ли файл и его создание
    """
    global database_filename
    if not os.path.exists(database_filename):
        with open(database_filename, "w") as f:
            f.close()


def add():
    """
    Добавление введеного числа в файл
    """
    global database_filename
    data = input("Введите число:")
    if data.isdigit():
        with open(database_filename, "a") as f:
            f.write(data + ",")
    else:
        print("Нужно вводить только цифры")
        add()


def print_data():
    """
    Вывод сохраненных в файле чисел
    """
    global database_filename
    with open(database_filename, "r") as f:
        database = f.read().split(",")[:-1]

    if len(database) == 0:
        print("No data")

    for i in database:
        print(i)


def delete():
    """
    Очистка файлв
    """
    global database_filename
    with open(database_filename, "w") as f:
        f.close()


def calculate():
    """
    Суммирование чисел в файле
    """
    global database_filename
    with open(database_filename, "r") as f:
        database = f.read().split(",")[:-1]
    sum = 0
    for i in database:
        sum = sum + int(i)
    print(f"Сумма чисел в файле равна {sum}")


def print_menu(menu):
    for i, m in enumerate(menu, start=1):
        print(f"{i}. {m}")


def get_command(menu):
    command = int(input("Input commmand: "))

    if 1 <= command <= len(menu):
        return command
    else:
        return -1


database_filename = "data.txt"

menu = ["Добавить", "Удалить", "Распечатать", "Посчитать", "Exit"]
commands = [add, delete, print_data, calculate, exit]

is_data()

while True:
    print_menu(menu)
    command = get_command(menu)

    if command == -1:
        print("Wrong command!")
        continue

    commands[command - 1]()
