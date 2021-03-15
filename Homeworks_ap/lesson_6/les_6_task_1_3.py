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

a = int(input('Введите трёхзначное число: '))

summ_ = (a // 100) + ((a // 10) % 10) + (a % 10)
mult_ = (a // 100) * ((a // 10) % 10) * (a % 10)

print(f'Сумма цифр во введённом числе {a} = {summ_}')
print(f'Произведение цифр во введённом числе {a} = {mult_}')

variable = (a, summ_, mult_)
lst = [i for i in (variable)]
show(lst)
