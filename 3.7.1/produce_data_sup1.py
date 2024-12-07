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

