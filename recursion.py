import timeit
import matplotlib.pyplot as plt

state = """def Fibonacci(n):
    if n < 0:
        return ("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

Fibonacci(32)"""

time = (timeit.repeat(stmt=state, number=1, repeat=5))
for item in time:
    print("{:.8f}".format(item))
plt.plot(time, 'g-o')
plt.show()