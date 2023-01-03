# Напишите программу, которая найдёт произведение
# пар чисел списка.
# Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# in  -> 4
# out -> [2, 5, 8, 10]
#     -> [20, 40]

from random import sample
import os
def clear(): return os.system('cls')


clear()

def get_mult_list (user_lenth):
    new_list = sample(range(1, user_lenth+1), k=user_lenth)
    return new_list
    
def get_mult_pair(some_list):  
    mult_list = []
    if len(some_list)%2!=0:
        for i in range(len(some_list)//2):
            mult_list.append(some_list[i]*some_list[len(some_list)-i-1])
        mult_list.append((some_list[len(some_list)//2]))
    else:
        for i in range(len(some_list)//2):
            mult_list.append(some_list[i]*some_list[len(some_list)-i-1])
    print(mult_list)

m = get_mult_list(int(input("Enter the number of items - ")))
print(m)
get_mult_pair(m)