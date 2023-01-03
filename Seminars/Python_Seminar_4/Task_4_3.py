# 3. На вход программе подается число n.
# Программа печатает численный треугольник.
# Используем вложенные циклы.

from math import sqrt

import os
def clear(): return os.system('cls')
clear()

n = int(input('Enter value - '))
for i in range(n+1):
    for k in range(i):
        print(i, end='')
    print()