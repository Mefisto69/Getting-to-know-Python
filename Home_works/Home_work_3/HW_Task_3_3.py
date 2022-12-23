# 3. Напишите программу, которая будет 
# преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# Пример:
# in  -> 88
# out -> 1011000

import os
def clear(): return os.system('cls')
clear()

def get_binary_number(user_decimal_number):
    decimal_number = []
    while user_decimal_number%2 !=0:
        decimal_number.append(user_decimal_number/2)
    print(reversed(decimal_number))
# остаток от деления на 2
# можно перевести в список и развернуть
get_binary_number(int (input("Введите число - ")))