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
    binary_number = []
    while user_decimal_number > 0:
        binary_number.insert(0,user_decimal_number % 2)
        user_decimal_number //=2
    print(*binary_number,sep="")
get_binary_number(int(input("Введите число - ")))