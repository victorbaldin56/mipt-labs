import sys

filename = sys.argv[1]
with open(filename, 'r') as f:
        lines = f.readlines()

U_data = []
I_data = []
NU_data = []

for line in lines:
    # in file order
    NU, U, I = map(float, line.split())
    U_data.append(U)
    I_data.append(I / (10 ** 3))
    NU_data.append(NU)


bebra_data = []
for i in range(len(U_data)):
    calc_tmp = U_data[i] / (NU_data[i] * I_data[i])
    bebra_data.append(calc_tmp)
    print(calc_tmp)