# *Задайте список из произвольных вещественных чисел, 
# количество задаёт пользователь.
# Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# in  -> 5
# out -> [5.16, 8.62, 6.57, 7.92, 9.22]
#     -> Min: 0.16, Max: 0.92. Difference: 0.76

import random

import os
clear = lambda: os.system('cls')
clear()

def get_float_list(user_length):
    new_list = []
    for i in range(user_length):
        new_list.append(round(random.uniform(1, 10), 2))
    return(new_list)

def get_cut_list(some_list):
    cut_list = [round(i%1,2) for i in some_list]
    return(cut_list)

float_list =get_float_list(int(input('Enter length - ')))
print(float_list)
print('Min: ',(min(get_cut_list(float_list))),
      'Max: ',(max(get_cut_list(float_list))),
      'Difference: ',round((max(get_cut_list(float_list)))-(min(get_cut_list(float_list))),2))