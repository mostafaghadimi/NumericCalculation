# http://sadeghsalmani.ir/post/153

import math
import matplotlib.pyplot as plot

h = 0.1

data = {
    'euler': {
        1: [0, 3]
    },
    'real': {
        1: [0, 3]
    }
}

# Calculate Euler
def Euler(x, i):
    y = data.euler.get(i - 1)[1]
    derivative_y = -2 * y
    temp_new_y = y + h * derivative_y
    derivative_temp_new_y = -2 * temp_new_y
    newY = data.euler.get(i - 1)[1] + (h / 2) * (derivative_y + derivative_temp_new_y)
    data.euler[i] = [x, newY]


x, i = 0, 2
while True:
    x += 0.1
    x = round(x, 1)
    Euler(x, i)
    i += 1
    if x == 20:
        break

# Calculate Real
def Real(x):
    return math.exp(-2 * x) * 3


x, i = 0, 2
while True:
    x += 0.1
    x = round(x, 1)
    y = Real(x)
    data.real[i] = [x, y]
    i += 1
    if x == 20:
        break

euler_x = []
euler_y = []

for j in range(1, 20):
    euler_x.append(data.euler.get(j)[0])
    euler_y.append(data.euler.get(j)[1])

# Euler Data
plot.plot(euler_x, euler_y, 'r--')
plot.ylabel('Euler Data')
plot.show()

real_x = []
real_y = []

for j in range(1, 20):
    real_x.append(data.real.get(j)[0])
    real_y.append(data.real.get(j)[1])

# Real Data
plot.plot(real_x, real_y)
plot.ylabel('Real Data')
plot.show()

# Compare
plot.plot(euler_x, euler_y, 'r--', real_x, real_y)
plot.ylabel('Real vs Euler')
plot.show()