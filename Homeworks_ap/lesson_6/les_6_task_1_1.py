'''
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
эффективным использованием памяти.
'''
'''
Найти сумму и произведение цифр трехзначного числа,
которое вводит пользователь.
'''
import sys

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

x = int(input('Введите трёхзначное число: '))

y1 = x // 100
y2 = x // 10 % 10
y3 = x % 10

z = y1 + y2 + y3
z2 = y1 * y2 * y3

print(f'Сумма цифр во введённом числе {x} = {z}')
print(f'Произведение цифр во введённом числе {x} = {z2}')

variable = (x, y1, y2, y3, z, z2)
lst = [i for i in (variable)]
show(lst)
