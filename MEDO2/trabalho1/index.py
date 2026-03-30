import numpy as np
import matplotlib.pyplot as plt

L = 0.1
T_inf = 10
K = 150
H = 450
err = 0.01
n = 10
step = L / (n - 1)
T = np.zeros((n, n))

T[n - 1, :] = 50
T[:, 0] = 100
T[0, :] = 75
T[0, 0] = 100

T[1 : n - 1, 1 : n - 1] = 60

erro_max = 1.0

while erro_max > err:
    erro_max = 0.0

    # pontos internos
    for i in range(1, n - 1):
        for j in range(1, n - 2):
            T_old = T[i, j]
            T[i, j] = (T[i + 1, j] + T[i - 1, j] + T[i, j + 1] + T[i, j - 1]) / 4
            diferenca = abs(T[i, j] - T_old)
            if diferenca > erro_max:
                erro_max = diferenca

    # coluna imediatamente anterior à fronteira direita
    for i in range(1, n - 1):
        j = n - 2
        T_old = T[i, j]
        T[i, j] = (
          (T[i + 1, j] + T[i - 1, j] + T[i, j - 1] + (H * T_inf)/((K / step) + H))
          /
          (4 - (K / step) / ((K / step) + H))
        )
        diferenca = abs(T[i, j] - T_old)
        if diferenca > erro_max:
            erro_max = diferenca

    # fronteira direita
    for i in range(1, n - 1):
        j = n - 1
        T_old = T[i, j]
        T[i, j] = (
          ((K / step) / ((K / step) + H)) * T[i, j - 1] + (H * T_inf)
          /
          ((K / step) + H)
        )
        diferenca = abs(T[i, j] - T_old)
        if diferenca > erro_max:
            erro_max = diferenca

    T[n - 1, :] = 50
    T[:, 0] = 100
    T[0, :] = 75
    T[0, 0] = 100

print(np.round(T, 4))

x = np.linspace(0, L, n)
y = np.linspace(0, L, n)
X, Y = np.meshgrid(x, y)

plt.figure(figsize=(7, 5))
plt.contourf(X, Y, T, levels=20)
plt.colorbar()
plt.contour(X, Y, T, levels=10, colors="black")
plt.show()

plt.figure(figsize=(7, 5))

plt.imshow(T, origin="upper", extent=[0, L, 0, L])
plt.colorbar(label="Temperatura (°C)")

plt.title("Mapa de Calor da Placa")
plt.xlabel("x (m)")
plt.ylabel("y (m)")

plt.savefig("./mapa_calor.png", dpi=300, bbox_inches="tight")

