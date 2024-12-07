import sys
import matplotlib.pyplot as plt
import numpy as np

filename_def = sys.argv[1]
with open(filename_def, 'r') as f:
        lines = f.readlines()

x_data = []
y_data = []

sumX = 0
sumY = 0
for line in lines:
  x, y = map(float, line.split())
  x_data.append(x)
  y_data.append(y)

print('avg x: ', sum(x_data)/len(x_data))
print('avg y: ', sum(y_data)/len(y_data))