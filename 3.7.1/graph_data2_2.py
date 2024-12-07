# i dont know what graph_data2 does so new one

import sys
import matplotlib.pyplot as plt
import numpy as np

filename = "data2_1div_freq2.txt"
with open(filename, 'r') as f:
        lines_freq = f.readlines()


filename = "data2_nu2.txt"
with open(filename, 'r') as f:
        lines_nu = f.readlines()

freq_data     = []
nu_data       = []
freq_err_data = []
nu_err_data   = []

# sigma_nu = 0.01
for line in lines_freq:
    freq, freq_err = map(float, line.split())
    freq_data.append(freq)
    freq_err_data.append(freq_err)

for line in lines_nu:
    nu, nu_err = map(float, line.split())
    nu_data.append(nu)
    nu_err_data.append(nu_err)

# x = np.linspace(-0.01, 0.32, len(bebra_data))

x = [450, 12700]
plt.plot(x, [x_ * (0.09731) + 2752 for x_ in x], color="red")
# plt.errorbar(nu_data, bebra_data, yerr=bebra_err_data, xerr=nu_err_data, color="red", fmt='.')
plt.errorbar(nu_data, freq_data, yerr=freq_err_data, xerr=nu_err_data, color="black", fmt='o')

plt.title("1 / ξ² = f(ν²)")
plt.ylabel("1 / ξ²")
plt.xlabel("ν²")

plt.show()