'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
import sys
import random
from random import randint

'''def show(obj):
    print(f'{type(obj)=}, {sys.getsizeof(obj)=}, {obj=}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                show(key)
                show(value)
        elif not isinstance(obj, str):
            for item in obj:
                show(item)'''

BIGNESS = 7
BEGIN = 0
END = 100

array = [random.randint(BEGIN, END) for _ in range(BIGNESS)]
print(f'Исходный массив - {array}')

min_ = min(array)
max_ = max(array)
imin_ = array.index(min_)
imax_ = array.index(max_)
print('array[%d]=%d array[%d]=%d' % (imin_+1, min_, imax_+1, max_))
array[imin_], array[imax_] = array[imax_], array[imin_]
print(array)