'''
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
'''

a = ord('a')
z = ord('z')

print('Введите номер буквы английского алфавита: ')
x = int(input('Введите от 1 до 26: '))

x = x + a - 1

if a <= x <= z:
    print(f"Вы ввели номер буквы {chr(x)}")
else:
    print('Введён неверный номер буквы')
