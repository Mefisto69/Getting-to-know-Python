# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in      -> out
# 6782    -> 23
# 0.67    -> 13
# 198.45  -> 27

import os
clear = lambda: os.system('cls')
clear()

User_value = float(input('Введите вещественное число: '))
while User_value != int(User_value):
    User_value *= 10
Result = 0
while User_value > 0:
    Result += User_value % 10
    User_value //= 10
print(int(Result))
