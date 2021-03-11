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

print(timeit.timeit('sum_num(10)', number = 1000, globals=globals()))       # 0.0013229000000000019
print(timeit.timeit('sum_num(50)', number = 1000, globals=globals()))       # 0.0053974999999999995
print(timeit.timeit('sum_num(100)', number = 1000, globals=globals()))      # 0.010947899999999997
print(timeit.timeit('sum_num(200)', number = 1000, globals=globals()))      # 0.020961499999999994
print(timeit.timeit('sum_num(500)', number = 1000, globals=globals()))      # 0.05364540000000001
print(timeit.timeit('sum_num(1_000)', number = 1000, globals=globals()))    # 0.11186770000000001

cProfile.run('sum_num(10)')
cProfile.run('sum_num(50)')
cProfile.run('sum_num(100)')
cProfile.run('sum_num(200)')
cProfile.run('sum_num(500)')
cProfile.run('sum_num(1_000)')

#        4 function calls in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 les_4_tsk_1.2.py:11(sum_num)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         4 function calls in 0.000 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 les_4_tsk_1.2.py:11(sum_num)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         4 function calls in 0.000 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 les_4_tsk_1.2.py:11(sum_num)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         4 function calls in 0.000 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 les_4_tsk_1.2.py:11(sum_num)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         4 function calls in 0.000 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 les_4_tsk_1.2.py:11(sum_num)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         4 function calls in 0.000 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 les_4_tsk_1.2.py:11(sum_num)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
