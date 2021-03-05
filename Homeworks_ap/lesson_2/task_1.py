'''
Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не завершается,
а запрашивает новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве
знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке и снова
запрашивать знак операции. Также она должна сообщать пользователю о невозможности
деления на ноль, если он ввел его в качестве делителя.
'''

while True:
    operation = input('Введите оператор вычисления +, -, *, / или 0 для выхода: ')
    if operation == '0':
        break
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))

    if operation == '+':
        c = a + b
    elif operation == '-':
        c = a - b
    elif operation == '*':
        c = a * b
    elif operation == '/':
        if b == 0:
            print('На ноль делить нельзя')
            continue
        c = a / b
    else:
        print('Не верный знак операции')
        continue
    print(f'{a} {operation} {b} = {c}')
