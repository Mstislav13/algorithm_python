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

print(timeit.timeit('sum_num(10)', number = 1000, globals=globals()))      # 0.0031032999999999894
print(timeit.timeit('sum_num(50)', number = 1000, globals=globals()))      # 0.017407999999999993
print(timeit.timeit('sum_num(100)', number = 1000, globals=globals()))     # 0.047560300000000014
print(timeit.timeit('sum_num(200)', number = 1000, globals=globals()))     # 0.1197021
print(timeit.timeit('sum_num(500)', number = 1000, globals=globals()))     # 0.3963468
print(timeit.timeit('sum_num(1_000)', number = 1000, globals=globals()))   # 1.0494811

cProfile.run('sum_num(10)')
cProfile.run('sum_num(50)')
cProfile.run('sum_num(100)')
cProfile.run('sum_num(200)')
cProfile.run('sum_num(500)')
cProfile.run('sum_num(1_000)')

#          14 function calls in 0.000 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 les_4_task_1.py:7(sum_num)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       10    0.000    0.000    0.000    0.000 {built-in method builtins.pow}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         54 function calls in 0.000 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 les_4_task_1.py:7(sum_num)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       50    0.000    0.000    0.000    0.000 {built-in method builtins.pow}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         104 function calls in 0.000 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 les_4_task_1.py:7(sum_num)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      100    0.000    0.000    0.000    0.000 {built-in method builtins.pow}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         204 function calls in 0.000 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 les_4_task_1.py:7(sum_num)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      200    0.000    0.000    0.000    0.000 {built-in method builtins.pow}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         504 function calls in 0.001 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#        1    0.000    0.000    0.001    0.001 les_4_task_1.py:7(sum_num)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      500    0.000    0.000    0.000    0.000 {built-in method builtins.pow}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#         1004 function calls in 0.001 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#        1    0.000    0.000    0.001    0.001 les_4_task_1.py:7(sum_num)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#     1000    0.001    0.000    0.001    0.000 {built-in method builtins.pow}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
