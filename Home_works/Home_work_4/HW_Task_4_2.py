# Задайте натуральное число N. 
# Напишите программу, которая составит 
# список простых множителей числа N.
# in  -> 54
# out -> [2, 3, 3, 3]
import os
clear = lambda: os.system('cls')
clear()

def get_mult_list(user_value:int):
   i = 2
   mult_list = []
   while i * i <= user_value:
       while user_value % i == 0:
           mult_list.append(i)
           user_value = user_value / i
       i = i + 1
   if user_value > 1:
       mult_list.append(user_value)
   return mult_list
print(get_mult_list(int(input("Enter a value - "))))