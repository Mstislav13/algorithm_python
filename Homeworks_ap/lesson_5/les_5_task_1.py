'''
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
(т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль
(за год для всех предприятий) и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.
'''
import collections

company = collections.namedtuple('company', ['q1', 'q2', 'q3', 'q4'])

year_profit = {}

num = int(input('Введите количество компаний: '))

for i in range(num):
    name = input(str( i + 1 ) + ' - я компания: ')
    profit_q1 = int(input('Введите прибыль компании за 1-ый квартал: '))
    profit_q2 = int(input('Введите прибыль компании за 2-ой квартал: '))
    profit_q3 = int(input('Введите прибыль компании за 3-ий квартал: '))
    profit_q4 = int(input('Введите прибыль компании за 4-ый квартал: '))
    year_profit[name] = company(q1 = profit_q1, q2 = profit_q2,
                                q3 = profit_q3, q4 = profit_q4)

total_profit = ()

for name, profit in year_profit.items():
    total_profit += profit                   # средняя прибыль компании за год

average_total_profit = sum(total_profit) / len(year_profit)
print('-//' * 20, '\n')
print(f'Средняя прибыль всех компаний за год - {average_total_profit} у.е.')

print('\n', '-//' * 20, '\n')
print('Компании, прибыль которых была выше среднего:')
for name, profit in year_profit.items():
    if sum(profit) > average_total_profit:
        print(f'Компания: {name} - {sum(profit)} у.е.')

print('\n', '-//' * 20, '\n')
print('Компании, прибыль которых была ниже среднего:')
for name, profit in year_profit.items():
    if sum(profit) < average_total_profit:
        print(f'Компания: {name} - {sum(profit)} у.е.')
