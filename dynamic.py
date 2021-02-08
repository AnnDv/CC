import timeit
import matplotlib.pyplot as plt

state = """def fibonacci(n):
    f = [0, 1]

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


print(fibonacci(32))"""

time = (timeit.repeat(stmt=state, number=1, repeat=5))
for item in time:
    print("{:.8f}".format(item))
plt.plot(time)
plt.show()