'''
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''
from collections import deque

def hex_sum(even, odd):
    num_ = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
            '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
            0 :'0', 1 :'1', 2 :'2', 3 :'3', 4 :'4', 5 :'5', 6 :'6', 7 :'7', 8 :'8',
            9 :'9', 10 :'A', 11 :'B', 12 :'C', 13 :'D', 14 :'E', 15 :'F'}
    result = deque()
    move = 0

    if len(odd) > len(even):
        even, odd = deque(odd), deque(even)
    else:
        even, odd = deque(even), deque(odd)

    while even:
        if odd:
            res = num_[even.pop()] + num_[odd.pop()] + move
        else:
            res = num_[even.pop()] + move
        move = 0

        if res < 16:
            result.appendleft(num_[res])
        else:
            result.appendleft(num_[res - 16])
            move = 1

    if move:
        result.appendleft('1')
    return list(result)

a = list(input('Введите 1-е шестнадцатиричное число: ').upper())
b = list(input('Введите 2-е шестнадцатиричное число: ').upper())

print(f' {a} + {b} = {hex_sum(a, b)}')
#print(*a, '+', *b, '=', *hex_sum(a, b))  # без скобок, кавычек и запятых
