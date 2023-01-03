# Вычислить число c заданной точностью d
# Пример:
# in  -> Enter a real number: 9
#     -> Enter the required accuracy '0.0001': 0.000001
# out -> 9.000000
# in  -> Enter a real number: 8.98785
#     -> Enter the required accuracy '0.0001': 0.001
# out -> 8.988
from decimal import *

import os
clear = lambda: os.system('cls')
clear()

user_number = Decimal(input('Enter a real number: '))
d_accuracy = Decimal(input('Enter the required accuracy "0.0001": '))
print(user_number.quantize(d_accuracy))