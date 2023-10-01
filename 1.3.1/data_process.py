import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import minimize

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

print(y)

a = [0] * 2
b = [0] * 2

colors = ['red', 'blue']
labels = ['acsending', 'descending']

fig = plt.figure(figsize=(6, 4))
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
