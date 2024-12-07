import numpy as np
import math
import sys
from scipy.optimize import curve_fit

def func(x, a, b):
    return x*a + b


filename = "data4.txt"
with open(filename, 'r') as f:
        lines = f.readlines()

nu_data = []
nu_err_data = []
psi_data = []
psi_err_data = []

# sigma_nu = 10

for line in lines:
    nu, nu_err, psi, psi_err = map(float, line.split())
    nu_data.append(nu)
    nu_err_data.append(nu_err)
    psi_data.append(psi * math.pi)
    psi_err_data.append(psi_err * math.pi)

popt, pcov = curve_fit(func, nu_data, psi_data, sigma=psi_err_data)
perr = np.sqrt(np.diag(pcov))

print('ax + b')
print('a       =', popt[0])
print('b       =', popt[1])
print('sigma a =', perr[0])
print('sigma b =', perr[1])
# print(popt)
# print(pcov)
# print(perr)