# Задача 18: Требуется найти в массиве 
# из случайных чисел(от 1 до n) самый 
# близкий по величине элемент к заданному 
# числу X. Пользователь в первой строке 
# вводит натуральное число N – количество 
# элементов в массиве. Последняя строка 
# содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint
array_size = int(input('Введите размер массива: '))
list_array = [randint(0, 9) for i in range(array_size)]
print(list_array)
search_x = int(input('Введите число х для поиска ближайщего: '))

res = list_array[0]
for i in list_array:
    if abs(i - search_x) < abs(res - search_x):
        res = i
print(res)