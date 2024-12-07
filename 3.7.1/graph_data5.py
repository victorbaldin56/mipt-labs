import sys
import matplotlib.pyplot as plt
import numpy as np

filename = "data5.txt"
with open(filename, 'r') as f:
        lines = f.readlines()

l_data = []
nu_data = []
l_err_data = []
nu_err_data = []

for line in lines:
    nu, nu_err, l, l_err = map(float, line.split())
    nu_data.append(nu)
    nu_err_data.append(nu_err)
    l_data.append(l * (10**(-3)))
    l_err_data.append(l_err * (10**(-3)))

# sigma = 0.001

# x = np.linspace(-0.01, 0.32, len(l_data))
# plt.plot([x_ for x_ in x], [x_ * (1090.6422) + 20.216 for x_ in x], color="black")
plt.errorbar(nu_data, l_data, yerr=l_err_data, xerr=nu_err_data, color="red", fmt='.')

plt.title("L = f(ν)")
plt.ylabel("L")
plt.xlabel("ν")

plt.show()