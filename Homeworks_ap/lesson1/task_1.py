'''
Найти сумму и произведение цифр трехзначного числа,
которое вводит пользователь.
'''

x = int(input('Введите трёхзначное число: '))

y1 = x // 100
y2 = x // 10 % 10
y3 = x % 10

z = y1 + y2 + y3
z2 = y1 * y2 * y3

print(f'Сумма цифр во введённом числе = {z}')
print(f'Произведение цифр во введённом числе = {z2}')
