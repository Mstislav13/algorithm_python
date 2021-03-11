'''
В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
'''

import random

BIGNESS = 10
BEGIN = 0
END = 50

array = [random.randint(BEGIN, END) for _ in range(BIGNESS)]
print(f'Исходный массив - {array}')

idx_min = 0
idx_max = 0
step = 1
total = 0

for i in array:
    if array[idx_min] > i:
        idx_min = array.index(i)
    elif array[idx_max] < i:
        idx_max = array.index(i)

if idx_max - idx_min < 0:
    step = -1

for i in array[idx_min + step:idx_max:step]:
    total += i
print(f'Сумма элементов между минимальным элементом {array[idx_min]}',
        f' и максимальным элементом {array[idx_max]} составляет {total}.')
