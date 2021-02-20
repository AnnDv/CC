import timeit

data_set = [1, 5, 9, 15, 20, 25, 40, 50]

def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


for i in data_set:
    start_time = timeit.default_timer()
    Fibonacci(i)
    print('Time for {:d}: {:.9f}'. format(i, timeit.default_timer() - start_time))




