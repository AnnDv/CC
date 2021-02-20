import timeit

MOD = 1000000007
data_set = [1, 5, 9, 15, 20, 25, 40, 50]

def FastDoubling(n, res):

    if (n == 0):
        res[0] = 0
        res[1] = 1
        return

    FastDoubling((n // 2), res)
    a = res[0]
    b = res[1]
    c = 2 * b - a

    if (c < 0):
        c += MOD
    c = (a * c) % MOD
    d = (a * a + b * b) % MOD

    if (n % 2 == 0):
        res[0] = c
        res[1] = d
    else:
        res[0] = d
        res[1] = c + d

res = [0] * 2

for i in data_set:
    start_time = timeit.default_timer()
    FastDoubling(i, res)
    print('Time for {:d}: {:.9f}'. format(i, timeit.default_timer() - start_time))