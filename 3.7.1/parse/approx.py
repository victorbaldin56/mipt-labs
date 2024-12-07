import numpy as np
import sys
from scipy.optimize import curve_fit

def func(x, a, b):
    return x*a + b


filename = sys.argv[1]
with open(filename, 'r') as f:
        lines = f.readlines()

x_data = []
y_data = []
x_err_data = []
y_err_data = []

for line in lines:
    # in file order
    x, x_err, y, y_err = map(float, line.split())
    x_data.append(x)
    y_data.append(y)
    x_err_data.append(x_err)
    y_err_data.append(y_err)

popt, pcov = curve_fit(func, x_data, y_data)
perr = np.sqrt(np.diag(pcov))

print('kx + b')
print('k       =', popt[0])
print('b       =', popt[1])
print('sigma k =', perr[0])
print('sigma b =', perr[1])
# print(popt)
# print(pcov)
# print(perr)