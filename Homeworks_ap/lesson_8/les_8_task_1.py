'''
Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных
подстрок в этой строке.
'''
def sub_str_count(string):
    subs = {}
    for j in range(len(string)):
        perc = ''
        for i, char in enumerate(string):
            if i + j < len(string):
                perc += string[i + j]
                subs.update({perc: subs[perc] + 1 if perc in subs else 1})
    return len(subs), subs

string = input('Введите строку: ')
print(f'Подстроки: {sub_str_count(string)[1]}')
print(f'Содержание: строка "{string}" и {(sub_str_count(string)[0]) - 1} подстрок.')
