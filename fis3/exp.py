import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

x = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
y = [8,5.8,4.3,3.4,2.7,2.25,1.92,1.62,1.44,1.24,1.1,1,0.88,0.80,0.72,0.65,0.58,0.54,0.5]
def modelo_inverso(x, a, alpha):
  return a / (x ** alpha)

params, _ = curve_fit(modelo_inverso, x[0:9], y[0:9], maxfev=10000)
a, alpha = params

y_fit = modelo_inverso(x, a, alpha)

print(alpha)

plt.scatter(x[0:9],y[0:9])
plt.plot(x[0:9], y_fit[0:9])
plt.grid()
plt.show()
# print(len(x))
# print(len(y))