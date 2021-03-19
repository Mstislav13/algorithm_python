'''
 Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
 заданный случайными числами на промежутке [0; 50).
 Выведите на экран исходный и отсортированный массивы.
'''
import random
from random import randint
from random import shuffle

SIZE = 10

def merge_list(list_1, list_2):
    list_0 = []
    x = 0
    y = 0
    while x < len(list_1) and y < len(list_2):
        if list_1[x] < list_2[y]:
            list_0.append(list_1[x])
            x += 1
        else:
            list_0.append(list_2[y])
            y += 1
    if x < len(list_1):
        list_0 += list_1[x:]
    if y < len(list_2):
        list_0 += list_2[y:]
    return list_0

def sort(list_):
    if len(list_) == 1:
        return list_
    middle = len(list_) // 2
    list_left = sort(list_[:middle])
    list_right = sort(list_[middle:])
    return merge_list(list_left, list_right)

array = [random.uniform(0, 50) for i in range(SIZE)]
shuffle(random.sample(array,0))
#------------------------------------------------------------------------------------------------
#array = [randint(0, 50) for _ in range(SIZE)] # При такой реализации сразу понятно, но не вещественные числа
#------------------------------------------------------------------------------------------------
#array = [float(i) for i in range(0, 50)]  # Голову сломал, не понял, как задать величину массива
#shuffle(array)
#------------------------------------------------------------------------------------------------
print(f'Исходный массив - {array}')
print(f'Отсортированный массив - {sort(array)}')
