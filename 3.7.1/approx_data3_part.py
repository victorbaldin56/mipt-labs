import numpy as np
import sys
from scipy.optimize import curve_fit

def func(x, a, b):
    return x*a + b


filename = "data3_part.txt"
with open(filename, 'r') as f:
        lines = f.readlines()

nu_data = []
nu_err_data = []
tg_data = []
tg_err_data = []

sigma_nu = 0.01

for line in lines:
    nu, tg, tg_err = map(float, line.split())
    nu_data.append(nu)
    nu_err_data.append(sigma_nu)
    tg_data.append(tg)
    tg_err_data.append(tg_err)

popt, pcov = curve_fit(func, nu_data, tg_data, sigma=tg_err_data)
perr = np.sqrt(np.diag(pcov))

print('ax + b')
print('a       =', popt[0])
print('b       =', popt[1])
print('sigma a =', perr[0])
print('sigma b =', perr[1])
# print(popt)
# print(pcov)
# print(perr)