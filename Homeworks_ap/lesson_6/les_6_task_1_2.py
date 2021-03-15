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

number = input('Введите трёхзначное число: ')

sum = 0
op = 1

for x in number:
    sum += int(x)
    op *= int(x)
print(f'Сумма цифр во введённом числе {number} = {sum}')
print(f'Произведение цифр во введённом числе {number} = {op}')

variable = (number, sum, op, x)
lst = [i for i in (variable)]
show(lst)
