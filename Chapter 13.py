# Chapter 13: Profiling and Optimizing Code

import cProfile

def slow_function():
    total = 0
    for i in range(10000):
        total += i
    return total

cProfile.run('slow_function()')