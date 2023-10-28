import random
import numpy as np
import matplotlib.pyplot as plt

y = []
x = np.linspace(0, 120, 200)
for i in range(len(x)):
    y.append(random.randint(i, i+25))

plt.scatter(x, y)
plt.show()