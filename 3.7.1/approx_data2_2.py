import numpy as np
import sys
from scipy.optimize import curve_fit

def func(x, a, b):
    return x*a + b

filename = "data2_1div_freq2.txt"
with open(filename, 'r') as f:
        lines_freq = f.readlines()


filename = "data2_nu2.txt"
with open(filename, 'r') as f:
        lines_nu = f.readlines()

freq_data     = []
nu_data       = []
freq_err_data = []
nu_err_data   = []

# sigma_nu = 0.01
for line in lines_freq:
    freq, freq_err = map(float, line.split())
    freq_data.append(freq)
    freq_err_data.append(freq_err)

for line in lines_nu:
    nu, nu_err = map(float, line.split())
    nu_data.append(nu)
    nu_err_data.append(nu_err)

popt, pcov = curve_fit(func, nu_data, freq_data, sigma=freq_err_data)
perr = np.sqrt(np.diag(pcov))

print('ax + b')
print('a       =', popt[0])
print('b       =', popt[1])
print('sigma a =', perr[0])
print('sigma b =', perr[1])
# print(popt)
# print(pcov)
# print(perr)