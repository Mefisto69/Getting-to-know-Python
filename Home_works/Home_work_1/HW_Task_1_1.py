# 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
import os
clear = lambda: os.system('cls')
clear()
User_number = int(input("Введите число, соответствующее номеру дня недели: "))
if User_number in range(1,6):
    print("Это рабочий день, увы =(")
elif User_number in range(6,8):
    print("Ура! =) Это выходной день!")
else:
    print("Такого дня не существует, попробуйте ещё раз =)")
    