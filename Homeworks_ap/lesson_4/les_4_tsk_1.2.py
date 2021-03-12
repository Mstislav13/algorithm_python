'''
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
'''
import timeit
import cProfile

def sum_num(b):
    i = 0
    next_ = 1
    step = -2
    sum_ = 0
    while i < b:
        next_ /= step
        sum_ += next_
        i += 1
    return sum_

print(timeit.timeit('sum_num(500)', number = 50, globals=globals()))      # 0.0028224000000000027
print(timeit.timeit('sum_num(1_000)', number = 50, globals=globals()))    # 0.005782800000000005
print(timeit.timeit('sum_num(10_000)', number = 50, globals=globals()))   # 0.057996500000000006
print(timeit.timeit('sum_num(20_000)', number = 50, globals=globals()))   # 0.11670469999999997
print(timeit.timeit('sum_num(30_000)', number = 50, globals=globals()))   # 0.1842931
print(timeit.timeit('sum_num(40_000)', number = 50, globals=globals()))   # 0.24975649999999994
print(timeit.timeit('sum_num(50_000)', number = 50, globals=globals()))   # 0.32330629999999994

cProfile.run('sum_num(500)')
cProfile.run('sum_num(1_000)')
cProfile.run('sum_num(10_000)')
cProfile.run('sum_num(20_000)')
cProfile.run('sum_num(30_000)')
cProfile.run('sum_num(40_000)')
cProfile.run('sum_num(50_000)')

#        4 function calls in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 les_4_tsk_1.2.py:7(sum_num)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         4 function calls in 0.000 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 les_4_tsk_1.2.py:7(sum_num)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         4 function calls in 0.001 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#        1    0.001    0.001    0.001    0.001 les_4_tsk_1.2.py:7(sum_num)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         4 function calls in 0.003 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#        1    0.003    0.003    0.003    0.003 les_4_tsk_1.2.py:7(sum_num)
#        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         4 function calls in 0.004 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#        1    0.004    0.004    0.004    0.004 les_4_tsk_1.2.py:7(sum_num)
#        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         4 function calls in 0.005 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#        1    0.005    0.005    0.005    0.005 les_4_tsk_1.2.py:7(sum_num)
#        1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         4 function calls in 0.006 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
#        1    0.006    0.006    0.006    0.006 les_4_tsk_1.2.py:7(sum_num)
#        1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
