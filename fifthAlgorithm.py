import math
from timeExecution import time_execution

def fifth_algorithm(n):
    c = [True] * n
    c[0] = False
    c[1] = False
    i = 2
    while i < n:
        j = 2
        while j < math.sqrt(i):
            if i % j == 0:
                c[i] = False
            j += 1
        i += 1

    return([i for i in range(n) if c[i]])

time_execution(fifth_algorithm)