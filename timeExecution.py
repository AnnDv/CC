import time
import matplotlib.pyplot as plt

def time_execution(prime_algorithm):

    n = [10, 100, 1000, 10000, 100000, 1000000]
    for i in n:
        start = time.time()
        prime_algorithm(i)
        end = time.time()
        print("Time execution of {:d}: {:.8f}".format(i, end - start))

        plt.plot(n, marker = "o")
        plt.show()