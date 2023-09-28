import matplotlib.pyplot as plt
import numpy as np

from data import x, f_x
from functions import lagrange

time = float(input(' Entre com o valor do tempo para o qual se deseja saber a posição aproximada(entre com 10, caso esteja seguindo o enunciado): '))

estimate_pos = lagrange(time)

print(f'A posição estimada quando t = {time}s é: {estimate_pos:.2f}')

for i in range(6):
    plt.scatter(x[i], f_x[i], color='blue')
plt.title('Estimativa da função deslocamento pela interpolação de Lagrange')
plt.xlabel('Tempo(s)')
plt.ylabel('Posição(pés)')
plt.grid()
plt.scatter(time, estimate_pos, color='yellow')
if(estimate_pos<lagrange(x[5])):
    plt.plot(np.linspace(x[0], x[5], 100), lagrange(np.linspace(x[0], x[5], 100)))
else:
    plt.plot(np.linspace(x[0], time, 100), lagrange(np.linspace(x[0], time, 100)))
plt.show()
