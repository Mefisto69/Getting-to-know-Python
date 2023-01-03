# Задайте строку из набора чисел.
# Напишите программу, которая покажет 
# наибольшее и наименьшее число.
# В качестве разделителя используйте пробел

import os
def clear(): return os.system('cls')
clear()

def chek_string():
    user_list = input('Enter a numbers - ').split()
    right_list = []
    for i in range(len(user_list)):
        user_list[i] = user_list[i].strip(".,;!/")
        if user_list[i].isdigit:
            right_list.append(user_list[i])
    print(right_list)
    return right_list

def max_min_value(right_list):
    return max(right_list, key=int),min(right_list,key=int)

print(max_min_value(chek_string()))