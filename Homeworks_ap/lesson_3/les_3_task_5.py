'''
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
'''

new_matrix = []

for i in range(4):
    new_matrix.append([])
    sum = 0
    for num_ in range(4):
        user_number = int(input(f'Введите {i+1} элемент {num_+1} столбца: '))
        sum += user_number
        new_matrix[i].append(user_number)

    new_matrix[i].append(sum)

for n in new_matrix:
    print(('{:>4d}' * 5).format(*n))
