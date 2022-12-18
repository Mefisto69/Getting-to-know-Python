# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# Пример:
# list [10]
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import os
clear = lambda: os.system('cls')
clear()
import random

N = int(input('Enter the lenght of the list: '))
Some_list = list(range(N))
print(Some_list)
for i in Some_list:
        Some_list [i] = random.randrange(N)
print(Some_list)