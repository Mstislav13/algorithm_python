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

print(timeit.timeit('sum_num(10)', number = 1000, globals=globals()))      # 0.003880400000000006
print(timeit.timeit('sum_num(50)', number = 1000, globals=globals()))      # 0.046385099999999985
print(timeit.timeit('sum_num(100)', number = 1000, globals=globals()))     # 0.1492053
print(timeit.timeit('sum_num(200)', number = 1000, globals=globals()))     # 0.5886387
print(timeit.timeit('sum_num(500)', number = 1000, globals=globals()))     # 3.9084835
print(timeit.timeit('sum_num(1_000)', number = 1000, globals=globals()))   # 15.922493900000001

cProfile.run('sum_num(10)')
cProfile.run('sum_num(50)')
cProfile.run('sum_num(100)')
cProfile.run('sum_num(200)')
cProfile.run('sum_num(500)')
cProfile.run('sum_num(1_000)')

#         14 function calls in 0.000 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 les_4_task_1.3.py:8(sum_num)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         54 function calls in 0.000 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 les_4_task_1.3.py:8(sum_num)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       50    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         104 function calls in 0.000 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 les_4_task_1.3.py:8(sum_num)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         204 function calls in 0.001 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#        1    0.001    0.001    0.001    0.001 les_4_task_1.3.py:8(sum_num)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      200    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         504 function calls in 0.006 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
#        1    0.006    0.006    0.006    0.006 les_4_task_1.3.py:8(sum_num)
#        1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
#      500    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         1004 function calls in 0.023 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.023    0.023 <string>:1(<module>)
#        1    0.022    0.022    0.023    0.023 les_4_task_1.3.py:8(sum_num)
#        1    0.000    0.000    0.023    0.023 {built-in method builtins.exec}
#     1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
