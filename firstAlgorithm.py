from timeExecution import time_execution

def first_algorithm(n):
    c = [True] * n
    c[0] = False
    c[1] = False
    i = 2
    while i < n:
        if c[i]:
            j = 2 * i
            while j < n:
                c[j] = False
                j = j + i
        i = i + 1

    return([i for i in range(n) if c[i]])

time_execution(first_algorithm)