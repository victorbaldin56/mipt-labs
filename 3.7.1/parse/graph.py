import sys
import matplotlib.pyplot as plt
import numpy as np

filename = sys.argv[1]
with open(filename, 'r') as f:
        lines = f.readlines()

x_data = []
y_data = []
x_err_data = []
y_err_data = []

for line in lines:
    x, x_err, y, y_err = map(float, line.split())
    x_data.append(x)
    y_data.append(y)
    x_err_data.append(x_err)
    y_err_data.append(y_err)

# sigma = 0.001

x = np.linspace(-0.01, 0.32, len(y_data))
plt.plot([x_ for x_ in x], [x_ * (1090.6422) + 20.216 for x_ in x], color="black")
plt.errorbar(x_data, y_data, yerr=y_err_data, xerr=x_err_data, color="red", fmt='.')

plt.show()