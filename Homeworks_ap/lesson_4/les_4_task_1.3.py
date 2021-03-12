'''
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
'''

import timeit
import cProfile

def sum_num(a):
    next_dig = -2
    sum_ = 0
    result = []
    for x in range(a):
        next_dig *= -0.5
        result.append(next_dig)
        for y in result:
            sum_ += y
    return result

print(timeit.timeit('sum_num(500)', number = 50, globals=globals()))       # 0.1864597
print(timeit.timeit('sum_num(1_000)', number = 50, globals=globals()))     # 0.699935
print(timeit.timeit('sum_num(10_000)', number = 50, globals=globals()))    # 67.6236888
print(timeit.timeit('sum_num(20_000)', number = 50, globals=globals()))    # 269.0083644
print(timeit.timeit('sum_num(30_000)', number = 50, globals=globals()))    # 611.5621128
print(timeit.timeit('sum_num(40_000)', number = 50, globals=globals()))    # 1090.8569518
print(timeit.timeit('sum_num(50_000)', number = 50, globals=globals()))    # 1744.7089130000002

cProfile.run('sum_num(500)')
cProfile.run('sum_num(1_000)')
cProfile.run('sum_num(10_000)')
cProfile.run('sum_num(20_000)')
cProfile.run('sum_num(30_000)')
cProfile.run('sum_num(40_000)')
cProfile.run('sum_num(50_000)')

#         504 function calls in 0.004 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#        1    0.004    0.004    0.004    0.004 les_4_task_1.3.py:8(sum_num)
#        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#      500    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         1004 function calls in 0.022 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.022    0.022 <string>:1(<module>)
#        1    0.022    0.022    0.022    0.022 les_4_task_1.3.py:8(sum_num)
#        1    0.000    0.000    0.022    0.022 {built-in method builtins.exec}
#     1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         10004 function calls in 1.576 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    1.576    1.576 <string>:1(<module>)
#        1    1.575    1.575    1.576    1.576 les_4_task_1.3.py:8(sum_num)
#        1    0.000    0.000    1.576    1.576 {built-in method builtins.exec}
#      100    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         20004 function calls in 5.883 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    5.883    5.883 <string>:1(<module>)
#        1    5.881    5.881    5.883    5.883 les_4_task_1.3.py:8(sum_num)
#        1    0.000    0.000    5.883    5.883 {built-in method builtins.exec}
#    20000    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         30004 function calls in 12.852 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000   12.852   12.852 <string>:1(<module>)
#        1   12.849   12.849   12.852   12.852 les_4_task_1.3.py:8(sum_num)
#        1    0.000    0.000   12.852   12.852 {built-in method builtins.exec}
#    30000    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         40004 function calls in 30.079 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000   30.079   30.079 <string>:1(<module>)
#        1   30.074   30.074   30.079   30.079 les_4_task_1.3.py:8(sum_num)
#        1    0.000    0.000   30.079   30.079 {built-in method builtins.exec}
#    40000    0.005    0.000    0.005    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         50004 function calls in 46.143 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000   46.143   46.143 <string>:1(<module>)
#        1   46.136   46.136   46.142   46.142 les_4_task_1.3.py:8(sum_num)
#        1    0.000    0.000   46.143   46.143 {built-in method builtins.exec}
#    50000    0.006    0.000    0.006    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
