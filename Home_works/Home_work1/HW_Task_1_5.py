# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# 
# in: 3, 6, 2, 1
# out: 5.099

import os
def clear(): return os.system('cls')
clear()

print("Найдём расстояние между 2-х точек в 2D пространстве")
xa = float(input('Введите координату точки "A" по оси "X":'))
ya = float(input('Введите координату точки "A" по оси "Y":'))
xb = float(input('Введите координату точки "B" по оси "X":'))
yb = float(input('Введите координату точки "B" по оси "Y":'))

import math
result = math.sqrt(((xb-xa)*(xb-xa))+((yb-ya)*(yb-ya)))
print(round(result,3))