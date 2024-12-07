import math
import sys

filename = "data5_pre_parse.txt"
with open(filename, 'r') as f:
        lines = f.readlines()

lmax = 9.88
sigma_lmax = 0.05

lmin = 2.89
sigma_lmin = 0.05

nu_data = []
nu_err_data = []
l_data = []
l_err_data = []

for line in lines:
    nu, nu_err, l, l_err = map(float, line.split())
    nu_data.append(nu)
    nu_err_data.append(nu_err)
    l_data.append(l)
    l_err_data.append(l_err)

for i in range(len(nu_data)):
    res_nu = nu_data[i]**2
    err_nu = 2 * nu_data[i] * nu_err_data[i]
    res_f = (lmax - l) / (l_data[i] - lmin)
    err_f = math.sqrt(  (((lmax - lmin) / ((l_data[i] - lmin)**2))**2) * (l_err_data[i]**2) + (((lmax - l_data[i]) / ((l_data[i] - lmin) ** 2))**2) * (sigma_lmin**2) + ((1/(l_data[i] - lmin))**2) * (sigma_lmax**2)  )
    print(res_nu, err_nu, res_f, err_f)