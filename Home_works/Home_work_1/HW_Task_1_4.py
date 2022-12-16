# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
# *Пример:*
# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти

import os
def clear(): return os.system('cls')
clear()

x = int(input("Чтобы узнать возможный диапазон точек в координатной четверти, введите её номер: "))
match x:
    case 1:
        print("x > 0, y > 0")
    case 2:
        print("x < 0, y > 0")
    case 3:
        print("x < 0, y < 0")
    case 4:
        print("x > 0, y < 0")
    case _:
        print("На координатной плоскости только 4 четверти")