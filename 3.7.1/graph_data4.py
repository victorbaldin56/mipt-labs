import math
import sys
import matplotlib.pyplot as plt
import numpy as np

filename = "data4.txt"
with open(filename, 'r') as f:
        lines = f.readlines()

nu_data = []
nu_err_data = []
psi_data = []
psi_err_data = []

# sigma_nu = 10

for line in lines:
    nu, nu_err, psi, psi_err = map(float, line.split())
    nu_data.append(nu)
    nu_err_data.append(nu_err)
    psi_data.append(psi * math.pi)
    psi_err_data.append(psi_err * math.pi)

# print("data parsed")

x = [33, 135]
# plt.plot([x_ for x_ in x], [x_ * 0.015682 + 0.41146 for x_ in x], color="black")
plt.plot([x_ for x_ in x], [x_ * 0.0146504 + 0.4635 for x_ in x], color="black")
plt.errorbar(nu_data, psi_data, yerr=psi_err_data, xerr=nu_err_data, color="red", fmt='.', capsize=3)

plt.title("ψ - π/4 = f(√ν)")
plt.ylabel("ψ - π/4")
plt.xlabel("√ν")

plt.show()