'''
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
'''

import random

BIGNESS = 10
BEGIN = 0
END = 100

array = [random.randint(BEGIN, END) for _ in range(BIGNESS)]
print(f'Исходный массив - {array}')

array_all = []
array_idx_even = []

for dig in array:
    array_all.append(array.index(dig))
print(f'Индексы всех элементов исходного массива - {array_all}')

for dig in array:
    if dig % 2 == 0:
        array_idx_even.append(array.index(dig))
print(f'Индексы чётных элементов исходного массива - {array_idx_even}.')
