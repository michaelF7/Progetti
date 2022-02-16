from os import system
from random import randrange

system("cls")

alist = [randrange(50) for i in range(10)]

for i in range(len(alist)):
    if i % 2 == 0:
        print(f"Indice: {i}, elemento: {alist[i]}")
