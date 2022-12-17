# 3. Задайте список из n чисел, 
# заполненный по формуле (1 + 1/n) ** n 
# и выведите на экран их сумму.
# Пример:
# in - 6
# out - [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# sum - 14.071

import os
clear = lambda: os.system('cls')
clear()

Some_list = []
n = int(input('Enter your value: '))
for n in range(1,n+1):
    Some_list.append(round((1+1/n) ** n,3))
print(Some_list)
print(round(sum(Some_list), 3))