'''
 Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
 Найдите в массиве медиану. Медианой называется элемент ряда,
 делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
 в другой — не больше медианы.
'''
import random

BIGNESS = 5
BEGIN = -50
END = 50
array = [random.randint(BEGIN, END) for _ in range(2 * BIGNESS + 1)]
print(f'Исходный массив: {array}')
def gnom(list_):
    i = 1
    size = len(list_)
    while i < size:
        if list_[i-1] <= list_[i]:
            i += 1
        else:
            list_[i-1], list_[i] = list_[i], list_[i-1]
            if i > 1:
                i -= 1
    return  list_
print(f'Отсортированный массив: {gnom(array)}')
idx = len(array) // 2
print(f'Индекс среднего числа (медианы): {idx}')
print(f'Медиана: {array[idx]}')

'''
Есть ещё вариант(наверное самый короткий):
import random
import statistics

BIGNESS = 5
BEGIN = -50
END = 50
array = [random.randint(BEGIN, END) for _ in range(2 * BIGNESS + 1)]
print(f'Исходный массив: {array}')
print(f'Медиана {statistics.median(array)}')
'''
