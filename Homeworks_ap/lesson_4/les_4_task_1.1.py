'''
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
'''
import timeit
import cProfile

def sum_num(a):
    summ = 0
    for i in range(a):
        summ += 1 / pow(-2, i)
    return summ

print(timeit.timeit('sum_num(500)', number = 50, globals=globals()))     # 0.020555199999999996
print(timeit.timeit('sum_num(1_000)', number = 50, globals=globals()))   # 0.053412299999999996
print(timeit.timeit('sum_num(10_000)', number = 50, globals=globals()))  # 4.5976672
print(timeit.timeit('sum_num(20_000)', number = 50, globals=globals()))  # 22.237982600000002
print(timeit.timeit('sum_num(30_000)', number = 50, globals=globals()))  # 54.738197400000004
print(timeit.timeit('sum_num(40_000)', number = 50, globals=globals()))  # 103.42958440000001
print(timeit.timeit('sum_num(50_000)', number = 50, globals=globals()))  # 168.2395601

cProfile.run('sum_num(500)')
cProfile.run('sum_num(1_000)')
cProfile.run('sum_num(10_000)')
cProfile.run('sum_num(20_000)')
cProfile.run('sum_num(30_000)')
cProfile.run('sum_num(40_000)')
cProfile.run('sum_num(50_000)')

#          504 function calls in 0.001 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#        1    0.000    0.000    0.001    0.001 les_4_task_1.1.py:7(sum_num)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      500    0.000    0.000    0.000    0.000 {built-in method builtins.pow}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         1004 function calls in 0.001 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#        1    0.001    0.001    0.001    0.001 les_4_task_1.1.py:7(sum_num)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#     1000    0.001    0.000    0.001    0.000 {built-in method builtins.pow}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         10004 function calls in 0.118 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.118    0.118 <string>:1(<module>)
#        1    0.009    0.009    0.118    0.118 les_4_task_1.1.py:7(sum_num)
#        1    0.000    0.000    0.118    0.118 {built-in method builtins.exec}
#    10000    0.109    0.000    0.109    0.000 {built-in method builtins.pow}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         20004 function calls in 0.489 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.489    0.489 <string>:1(<module>)
#        1    0.019    0.019    0.489    0.489 les_4_task_1.1.py:7(sum_num)
#        1    0.000    0.000    0.489    0.489 {built-in method builtins.exec}
#    20000    0.470    0.000    0.470    0.000 {built-in method builtins.pow}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         30004 function calls in 1.123 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    1.123    1.123 <string>:1(<module>)
#        1    0.027    0.027    1.123    1.123 les_4_task_1.1.py:7(sum_num)
#        1    0.000    0.000    1.123    1.123 {built-in method builtins.exec}
#    30000    1.097    0.000    1.097    0.000 {built-in method builtins.pow}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         40004 function calls in 2.068 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    2.068    2.068 <string>:1(<module>)
#        1    0.037    0.037    2.068    2.068 les_4_task_1.1.py:7(sum_num)
#        1    0.000    0.000    2.068    2.068 {built-in method builtins.exec}
#    40000    2.031    0.000    2.031    0.000 {built-in method builtins.pow}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
