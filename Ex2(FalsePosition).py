import matplotlib.pyplot as plt
from sympy import *


def f(x, f):
    return sympify(f).subs({'x': x}).evalf()


def false_position(a, b, max_iteration, f):
    lower_bound = f(a, f)
    upper_bound = f(b, f)
    if (lower_bound * upper_bound) > 0:
        print("Unsuitable initial points!")
        exit()
    elif lower_bound == 0:
        print("First point is the root!")
        exit()
    elif upper_bound == 0:
        print("Second point is the root!")
        exit()
    results = []
    for i in range(max_iteration):
        lower_bound = f(a, f)
        upper_bound = f(b, f)
        tmp = (a * upper_bound - b * lower_bound) / (upper_bound - lower_bound)
        results.append(tmp)
        temp = f(tmp, f)
        if temp == 0:
            print(i)
            return results
        elif temp * lower_bound > 0:
            a = tmp
        else:
            b = tmp
    return results


func = input("function:")
iteration = int(input("iteration: "))
a, b = list(map(float, input()))
answers = false_position(a, b, iteration, func)
print("The answer is:", answers[-1])
plot = plt.plot(range(answers.__len__()), answers)
plt.xlabel("iter")
plt.ylabel("estimated root")
plt.show()