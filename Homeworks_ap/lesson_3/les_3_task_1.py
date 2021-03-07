'''
В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''

result = {}
for x in range (2, 10):
    result [x] = []
    for multiple in range (2, 100):
        if multiple % x == 0:
            result [x].append(multiple)
    print(f'Числу {x} кратны {len(result [x])} чисел: {result[x]}.')
