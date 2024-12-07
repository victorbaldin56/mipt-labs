import sys
import matplotlib.pyplot as plt
import numpy as np

filename = "data3_part.txt"
with open(filename, 'r') as f:
        lines = f.readlines()

nu_data = []
nu_err_data = []
tg_data = []
tg_err_data = []

sigma_nu = 0.01

for line in lines:
    nu, tg, tg_err = map(float, line.split())
    nu_data.append(nu)
    nu_err_data.append(sigma_nu)
    tg_data.append(tg)
    tg_err_data.append(tg_err)

# print("data parsed")

x = [110, 710]
plt.plot([x_ for x_ in x], [x_ * (0.0071) - 0.025 for x_ in x], color="black")
plt.errorbar(nu_data, tg_data, yerr=tg_err_data, xerr=nu_err_data, color="red", fmt='.', capsize=3)

plt.title("tgψ = f(ν)")
plt.ylabel("tgψ")
plt.xlabel("ν")

plt.show()