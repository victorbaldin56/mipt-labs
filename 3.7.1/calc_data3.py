import math
import sys

filename = "data3.txt"
with open(filename, 'r') as f:
        lines = f.readlines()

nu_data = []
dphi_data = []
dphi_err_data = []

for line in lines:
    nu, dphi, dphi_err = map(float, line.split())
    nu_data.append(nu)
    dphi_data.append(dphi)
    dphi_err_data.append(dphi_err)

sigma_nu = 0.01

for i in range(len(nu_data)):
    res = math.tan(dphi_data[i] * math.pi)
    er = (dphi_err_data[i] * math.pi ) / (math.cos(dphi_err_data[i] * math.pi) ** 2)
    print(nu_data[i], res, er)