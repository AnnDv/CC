from timeExecution import time_execution

def second_algorithm(n):
    c = [True] * n
    c[0] = False
    c[1] = False
    i = 2
    while i <= n:
        j = 2 * i
        while j < n:
            c[j] = False
            j = j + i
        i = i + 1

    return([i for i in range(n) if c[i]])


time_execution(second_algorithm)