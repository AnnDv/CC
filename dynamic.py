import timeit

data_set = [1, 5, 9, 15, 20, 25, 40, 50]
def fibonacci(n):
    f = [0, 1]

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]

for i in data_set:
    start_time = timeit.default_timer()
    fibonacci(i)
    print('Time for {:d}: {:.9f}'. format(i, timeit.default_timer() - start_time))

