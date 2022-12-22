# Задайте список, состоящий из произвольных чисел, 
# количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётных позициях(не индексах).
# Пример:
# in  -> 5
# out -> [10, 2, 3, 8, 9]
#     -> 22
from random import sample
import os
def clear(): return os.system('cls')
clear()

def get_list (user_lenth):
    new_list = sample(range(1,user_lenth+1),k=user_lenth)
    print(new_list)
    sum = 0
    for i in range(0,len(new_list),2):
        sum += new_list[i]
    print(sum)

get_list(int(input("Enter the number of items - ")))