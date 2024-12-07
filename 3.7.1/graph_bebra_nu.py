import sys
import matplotlib.pyplot as plt
import numpy as np

filename = sys.argv[1]
with open(filename, 'r') as f:
        lines = f.readlines()

bebra_data = []
nu_data = []
bebra_err_data = []
nu_err_data = []

for line in lines:
    bebra, nu = map(float, line.split())
    bebra_data.append(bebra)
    nu_data.append(nu)
    bebra_err_data.append(0)
    nu_err_data.append(0)

# sigma = 0.001

x = np.linspace(-0.01, 0.32, len(bebra_data))
# plt.plot([x_ for x_ in x], [x_ * (1090.6422) + 20.216 for x_ in x], color="black")
plt.errorbar(nu_data, bebra_data, yerr=bebra_err_data, xerr=nu_err_data, color="red", fmt='.')

plt.show()