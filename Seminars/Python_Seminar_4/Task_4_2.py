# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
# с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
# Уравнения и корни запишите в файл.

from math import sqrt

import os
def clear(): return os.system('cls')
clear()

def find_root(a,b,c:int ):
    discriminant = b**2-4*a*c
    with open("Discrime.txt", "a", encoding="utf-8") as my_file:
        my_file.write(f"{a}x² + {b}x + {c} = 0\n")
        if discriminant>0:
            x1 = (-b- sqrt(discriminant))/(2*a)
            x2 = (-b+ sqrt(discriminant))/(2*a)
            my_file.write(f"{x1,x2}\n")
        elif discriminant == 0:
            x = -b /(2*a)
            my_file.write(f"{x}\n")
        else:
            my_file.write("Нет корней\n")

find_root(3,8,12)