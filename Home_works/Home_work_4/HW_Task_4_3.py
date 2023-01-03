# Задайте последовательность чисел. 
# Напишите программу, которая выведет 
# список неповторяющихся элементов 
# исходной последовательности в том же порядке.
# in  -> 7
# out -> [4, 5, 3, 3, 4, 1, 2]
#     -> [5, 1, 2]
# in  -> -1
# out -> Negative value of the number of numbers!
#     -> []
# in  -> 10
# out -> [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
#     -> [6, 2, 3, 0, 9]
from random import *

import os
clear = lambda: os.system('cls')
clear()

def get_list (user_lenth):
    if user_lenth<=0:
        print('Negative value of the number of numbers!')
        return []
    else:
        first_list = []
        for i in range(user_lenth+1):
            first_list.append(randrange(1,user_lenth))
        return (first_list)

def get_unical_numbers(some_list):
    unical_list = []
    for i in some_list:
        if some_list.count(i) == 1:
            unical_list.append(i)
    return(unical_list)

user_list = get_list(int(input("Enter the number of items - ")))
print(user_list)
print(get_unical_numbers(user_list))
