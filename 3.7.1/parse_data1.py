import math
import sys

filename = sys.argv[1]
with open(filename, 'r') as f:
        lines = f.readlines()

nu_data = []
u_data = []
i_data = []

for line in lines:
    nu, u, i = map(float, line.split())
    nu_data.append(nu)
    u_data.append(u)
    i_data.append(i)

sigma_nu = 0.01
sigma_u = 0.0001
sigma_i = 0.00001

for i in range(len(nu_data)):
    res = (nu_data[i] ** 2) * (i_data[i] ** 2) / (u_data[i] ** 2)
    er = res * math.sqrt(4 * ((sigma_i / i_data[i])** 2) + 4 * ((sigma_u / u_data[i])** 2) + 4 * ((sigma_nu / nu_data[i])** 2)) 
    print(res, er)
