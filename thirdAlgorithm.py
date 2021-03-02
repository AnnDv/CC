from timeExecution import time_execution

def third_algorithm(n):
    c = [True] * n
    c[0] = False
    c[1] = False
    i = 2
    while i < n:
        if c[i]:
            j = i + 1
        while j < n:
            if (j % i == 0):
                c[j] = False
            j = j + 1
        i = i + 1

    return([i for i in range(n) if c[i]])

time_execution(third_algorithm)