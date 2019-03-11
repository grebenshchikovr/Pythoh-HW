import os


def dir_path(x):
    dir_name = "dir_" + str(x)
    return os.path.join(os.getcwd(), dir_name)


for i in range(1, 10):
    try:
        os.mkdir(dir_path(i))
    except FileExistsError:
        print('Такая директория уже существует')

for i in range(1, 10):
    try:
        os.rmdir(dir_path(i))
    except FileNotFoundError:
        print('Такая директория не существует')

