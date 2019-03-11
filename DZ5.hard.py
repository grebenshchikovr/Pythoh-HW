import os
import sys

BASE_PATH = r"D:\Python_school\test"
# Определить какие у меня в папке расширения у файлов
ext = set()
for i in os.listdir(BASE_PATH):
    if os.path.isfile(os.path.join(BASE_PATH, i)):
        print(os.path.splitext(i))
        ext.add(os.path.splitext(i)[1])  # добавить в множество расширение текущего файла

# print(ext)
# Создаем папки
for e in ext:
    if not os.path.exists(os.path.join(BASE_PATH, e)):
        os.mkdir(os.path.join(BASE_PATH, e))

# Переносим файлы в соответствующие каталоги
for i in os.listdir(BASE_PATH):
    if os.path.isfile(os.path.join(BASE_PATH, i)):
        os.rename(os.path.join(BASE_PATH, i),
                  os.path.join(BASE_PATH, os.path.splitext(i)[1], i))

answer = input("Вернем файлы в корень? Y/N")
if answer.lower() == "n":
    exit()
elif answer.lower() == "y":
    pass
else:
    print("недопустимый ответ, будем считать, что нет")
    exit()

# переносим файлы на уровень выше
for i in os.listdir(BASE_PATH):
    if os.path.isdir(os.path.join(BASE_PATH, i)):

        for j in os.listdir(os.path.join(BASE_PATH, i)):
            if os.path.isfile(os.path.join(BASE_PATH, i, j)):
                os.rename(os.path.join(BASE_PATH, i, j),
                          os.path.join(BASE_PATH, j))

# удаляем папки
for i in os.listdir(BASE_PATH):
    if os.path.isdir(os.path.join(BASE_PATH, i)):
        os.rmdir(os.path.join(BASE_PATH, i))
