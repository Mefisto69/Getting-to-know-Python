# Задайте список, состоящий из произвольных слов
# количество задаёт пользователь.
# Напишите программу, которая определит индекс
# второго вхождения строки в списке,
# либо сообщит, что её нет

import os
clear = lambda: os.system('cls')
clear()

from random import sample

def words_list(quantity_words, chars_for_list_gen='abc'):   # в метод вводим количество слов
                                                            # и символы для формирования слов
    new_list = []
    for i in range(quantity_words):
        x = sample(chars_for_list_gen,k=3)
        new_list.append("".join(x))
    return new_list

def find_second_value(some_list,find_word):
    if find_word in some_list and some_list.count(find_word)>1:
        fist_value = some_list.index(find_word)
        print(some_list.index(find_word,fist_value+1))
    else:
        print(-1)

n = words_list(int(input('Введите количество слов - ')))
print(n)
find_second_value(n,input('Введите слово - '))