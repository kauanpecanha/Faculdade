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

for i in range(0, len(x2)):
  xiyi = xiyi + x2[i]*y2[i]

  yi = yi + y2[i]

  xi = xi + x2[i]

  xi2 = xi2 + ((x2[i])**2)

b2 = (
    (xiyi - (1/len(x2))*(xi*yi))
    /
    (xi2 - (1/len(x2)*((xi)**2)))
)

a2 = (((1/len(x2)*(yi))) - ((b2/len(x2)) * (xi)))

print(a2, b2)

plt.grid()
plt.scatter(x2, y2)
plt.plot(x2, function(x2, a2, b2))
plt.title('Exercício 2')
plt.xlabel('Valores de x')
plt.ylabel('Valores de y')
plt.show()
