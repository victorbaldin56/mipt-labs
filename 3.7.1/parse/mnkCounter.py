from math import *
import sys

filename = sys.argv[1]
with open(filename, 'r') as f:
    lines = f.readlines()

arrayX = []
arrayY = []

for line in lines:
    x, y = map(float, line.split())
    arrayX.append(x)
    arrayY.append(y)

if len(arrayX) != len(arrayY):
  print("shit happends")
else:
  n = len(arrayX)
  sumX = sum(arrayX) / n
  sumY = sum(arrayY) / n

  sumXY = 0
  for i in range(0, n):
    sumXY += arrayX[i]*arrayY[i]
  sumXY /= n

  sumX2 = sum([x**2 for x in arrayX]) / n
  sumY2 = sum([y**2 for y in arrayY]) / n

  a = (sumXY - sumX*sumY) / (sumX2 - sumX**2)
  b = sumY - a*sumX

  deltaA = (1/sqrt(n))* sqrt(abs(       ((sumY2 - sumY**2) / (sumX2 - sumX**2)) - a**2)              )
  deltaB = deltaA*sqrt(abs(sumX2-sumX**2))

  k = sumXY / sumX2
  deltaK = (1/sqrt(n))*sqrt((sumY2 / sumX2) - k**2)

  print("ax + b or kx:")
  print("a coef: ", a)
  print("b coef: ", b)
  print("delta a: ", deltaA)
  print("delta b: ", deltaB)
  print("k coef: ", k)
  print("delta k: ", deltaK)
