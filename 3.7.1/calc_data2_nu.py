import math
import sys

filename = "data2_nu.txt"
with open(filename, 'r') as f:
        lines = f.readlines()

nu_data = []

for line in lines:
    nu = float(line)
    nu_data.append(nu)

sigma_nu = 0.01

for i in range(len(nu_data)):
    res = nu_data[i] ** 2
    er = 2 * nu_data[i] * sigma_nu
    print(res, er)