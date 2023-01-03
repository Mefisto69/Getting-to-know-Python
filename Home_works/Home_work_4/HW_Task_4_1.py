# Вычислить число c заданной точностью d
# Пример:
# in  -> Enter a real number: 9
#     -> Enter the required accuracy '0.0001': 0.000001
# out -> 9.000000
from decimal import *

import os
clear = lambda: os.system('cls')
clear()

user_number = Decimal(int(input('Enter a real number: ')))
d_accuracy = Decimal(input('Enter the required accuracy "0.0001": '))
print (user_number-d_accuracy+d_accuracy)