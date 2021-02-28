'''
По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника, составленного из этих отрезков.
Если такой треугольник существует, то определить, является ли он разносторонним,
равнобедренным или равносторонним.
'''
print('Введите размер трёх сторон треугольника: ')
a = float(input('Введите первую сторону треугольника: '))
b = float(input('Введите вторую сторону треугольника: '))
c = float(input('Введите третью сторону треугольника: '))

if a + b > c and b + c > a and a + c >b:
    if a == b and b == c and a == c:
        print('Это равносторонний треугольник')
    elif a == b or b == c or a == c:
        print('Это равнобедренный треугольник')
    else:
        print('Это раpносторонний треугольник')
else:
    print('Это не треугольник')
