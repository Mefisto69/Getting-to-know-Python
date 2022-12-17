# 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

import os
clear = lambda: os.system('cls')
clear()

Empty_list = []
N = int(input('Enter the value of N: '))
for i in range (-N,N+1):
    Empty_list.append(i)
print(Empty_list)
print(Empty_list[(int(input('Position one: ')))-1]*Empty_list[(int(input('Position two: ')))-1])