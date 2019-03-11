#import sys
import os

m = int(input("Введите M: "))
for _ in range(m):
    n = input("Введите N: ")
    s = input("Введите текст S: ")

    os.system(f"python DZ5.normal1.py {n} {s}")
