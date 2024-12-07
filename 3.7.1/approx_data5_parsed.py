import numpy as np
import math
import sys
from scipy.optimize import curve_fit

def func(x, a, b):
    return x*a + b


filename = "data5_parsed.txt"
with open(filename, 'r') as f:
        lines = f.readlines()

nu2_data = []
nu2_err_data = []
fraq_data = []
fraq_err_data = []

for line in lines:
    nu2, nu2_err, fraq, fraq_err = map(float, line.split())
    nu2_data.append(nu2)
    nu2_err_data.append(nu2_err)
    fraq_data.append(fraq)
    fraq_err_data.append(fraq_err)

popt, pcov = curve_fit(func, nu2_data, fraq_data, sigma=fraq_err_data)
perr = np.sqrt(np.diag(pcov))

print('ax + b')
print('a       =', popt[0])
print('b       =', popt[1])
print('sigma a =', perr[0])
print('sigma b =', perr[1])
# print(popt)
# print(pcov)
# print(perr)