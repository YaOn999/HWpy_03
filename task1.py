# Задача 16: Требуется вычислить, сколько раз 
# встречается некоторое число X в массиве из 
# случайных чисел. Пользователь в первой строке 
# вводит натуральное число N – количество элементов 
# в массиве. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1
from random import randint
array_size = int(input('Введите размер массива: '))
list_array = [randint(0, 9) for i in range(array_size)]
print(list_array)
search_x = int(input('Введите число х для поиска: '))

result = list_array.count(search_x)
print(result)