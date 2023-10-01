import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
# from scipy.optimize import minimize
import statistics as stat
import math

matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

lerm = pd.read_csv('data/lermantov.csv')

# Getting data series from our dataframe
x = lerm.iloc[:, 1]

y = []
for i in range(2, 6):
    y.append(lerm.iloc[:, i])

# print(y)

a = [0] * 2
b = [0] * 2

colors = ['red', 'blue']
labels = ['acsending', 'descending']

fig = plt.figure(figsize=(5, 4))
# f, (ax1, ax2) = plt.subplots(1, 2, sharey = True)

for i in range(2):
    a[i], b[i] = np.polyfit(x, y[i], 1)
    plt.scatter(x, y[i], color = colors[i], label = labels[i])
    # plt.scatter(x, a[i + 2] * x + b[i + 2], color = colors[i], label = labels[i])

    plt.plot(x, a[i] * x + b[i], label = '$y = {0:.2f}x + {1:.2f}$'.format(a[i], b[i]), color =
             colors[i])
    # ax2.plot(x, a[i + 2] * x + b[i + 2])

# plt.scatter(x, y[0], color = 'red', label = 'ascending')
# plt.plot(x, a[0] * x + b[0], color = "red")
#
# plt.scatter(x, y[1], color = 'blue', label = 'descending')
# plt.plot(x, a[1] * x + b[1], color = "blue")
#
plt.grid(linestyle = '--')
plt.legend()

plt.xlabel('$P$, N$')
plt.ylabel('$n$, cm')

plt.savefig('graphs/lermant.pgf')

# arithmetic mean of k
coeff_k = stat.mean(a)

# squares
x_sq = [P ** 2 for P in x]
y_sq = [n ** 2 for n in y[0]]

# error of coeff_k
eps_k = 1 / (coeff_k * math.sqrt(3)) * math.sqrt((stat.mean(y_sq) - stat.mean(y[0]) ** 2
                                                  ) / (stat.mean(x_sq) -
                                                       stat.mean(x) ** 2) - coeff_k ** 2)

print(eps_k)
