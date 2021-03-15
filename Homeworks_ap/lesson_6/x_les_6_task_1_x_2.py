'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
import sys
from random import randint

def show(obj):
    print(f'{type(obj)=}, {sys.getsizeof(obj)=}, {obj=}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                show(key)
                show(value)
        elif not isinstance(obj, str):
            for item in obj:
                show(item)


go = True

while go:
    items_cnt = int(input('Введите количество элементов в списке: '))
    array = [randint(-100, 100) for _ in range(items_cnt)]
    min_value_idx = max_value_idx = 0
    max_value = min_value = array[0]

    print(array)

    for idx in range(1, len(array)):
        if array[idx] > max_value:
            max_value_idx, max_value = idx, array[idx]
        elif array[idx] < min_value:
            min_value_idx, min_value = idx, array[idx]

    array[min_value_idx], array[max_value_idx] = array[max_value_idx], array[min_value_idx]
    break
print(array)

variable = (go, items_cnt, array, min_value_idx, max_value_idx, idx)
lst = [i for i in (variable)]
show(lst)
