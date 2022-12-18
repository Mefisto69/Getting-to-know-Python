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
        j = random.randrange(N)
        Some_list[i],Some_list[j] = Some_list[j],Some_list[i]
print(Some_list)