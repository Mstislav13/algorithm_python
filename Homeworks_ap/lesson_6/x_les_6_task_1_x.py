'''
Попробвал ещё пару других задач.
'''
'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
import sys
import random

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

BIGNESS = 7
BEGIN = 0
END = 100

array = [random.randint(BEGIN, END) for _ in range(BIGNESS)]
print(f'Исходный массив - {array}')

max_el = array[0]
min_el = array[0]

for i in array:
    if i > max_el:
        max_el = i
    elif i < min_el:
        min_el = i

idx_max = array.index(max_el)
idx_min = array.index(min_el)
array[idx_max], array[idx_min] = array[idx_min], array[idx_max]

print(f'После замены в исходном массиве максимального элемента - {max_el} с индексом ({idx_max}) '
      f'на минимальный элемент - {min_el} с индексом ({idx_min}):'
      f'\n исходный массив будет выглядеть - {array}.')

variable = (BIGNESS, BEGIN, END, array, max_el, min_el, idx_max, idx_min, i)
lst = [i for i in (variable)]
show(lst)
