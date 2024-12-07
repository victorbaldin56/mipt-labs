import math
import sys

filename = "data4_pre.txt"
with open(filename, 'r') as f:
        lines = f.readlines()

nu_data = []

for line in lines:
    nu = float(line)
    nu_data.append(nu)

sigma_nu = 10

for i in range(len(nu_data)):
    # res = math.tan(dphi_data[i] * math.pi)
    # er = (dphi_err_data[i] * math.pi ) / (math.cos(dphi_err_data[i] * math.pi) ** 2)
    res = math.sqrt(nu_data[i])
    er = (sigma_nu) / (2 * math.sqrt(nu_data[i]))
    print(res, er)