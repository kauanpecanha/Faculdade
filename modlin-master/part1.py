import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([1, 1, 2, 2, 3, 3])
y1 = np.array([1, 3, 1, 3, 1, 3])

x2 = np.array([1, 2, 2, 3, 3, 4])
y2 = np.array([1, 1, 2, 2, 3, 3])

def function(x, a, b):
  return b*x + a

xiyi = 0
yi = 0
xi = 0
xi2 = 0

for i in range(0, len(x1)):
  xiyi = xiyi + x1[i]*y1[i]

  yi = yi + y1[i]

  xi = xi + x1[i]

  xi2 = xi2 + ((x1[i])**2)

b1 = (
    (xiyi - (1/len(x1))*(xi*yi))
    /
    (xi2 - (1/len(x1)*((xi)**2)))
)

a1 = (((1/len(x1)*(yi))) - ((b1/len(x1)) * (xi)))


print(a1, b1)

plt.grid()
plt.scatter(x1, y1)
plt.plot(x1, function(x1, a1, b1))
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.title('Exercício 1')
plt.show()