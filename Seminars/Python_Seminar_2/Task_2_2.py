# Создать список длинны N
# Значения формируются по формуле
# 3k+1 , где k принимает значение от 1 до N включительно
# Пример: in = 3 ; out = [4, 7, 10]
#         in = 6 ; out = [4, 7, 10, 13, 16, 19]

import os
clear = lambda: os.system('cls')
clear()

num_list = []
n = int(input("Введите число "))
for k in range(1,n+1):
    num_list.append(3*k+1)
print(num_list)