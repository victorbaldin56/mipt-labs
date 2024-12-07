import sys
import matplotlib.pyplot as plt
import numpy as np

filename = "data5_parsed.txt"
with open(filename, 'r') as f:
        lines = f.readlines()

nu2_data = []
nu2_err_data = []
fraq_data = []
fraq_err_data = []

for line in lines:
    nu2, nu2_err, fraq, fraq_err = map(float, line.split())
    nu2_data.append(nu2)
    nu2_err_data.append(nu2_err)
    fraq_data.append(fraq)
    fraq_err_data.append(fraq_err)

# sigma = 0.001

x = [2400, 65 * (10**4)]
plt.plot([x_ for x_ in x], [x_ * (2.699932 * (10**(-5))) + 0.814 for x_ in x], color="black")
plt.errorbar(nu2_data, fraq_data, yerr=fraq_err_data, xerr=nu2_err_data, color="red", fmt='.')

plt.title("f(ν²)")
plt.ylabel("f")
plt.xlabel("ν²")

plt.show()