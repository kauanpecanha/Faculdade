import numpy as np
import matplotlib.pyplot as plt

# 1. Parâmetros do problema
L = 1.0               # comprimento da barra (m)
u = 0.1               # velocidade de advecção (m/s)
n = 101               # número de nós
dt = 0.05             # passo de tempo (s)
t_total = 5.0         # tempo total (s)
TA = 100.0            # contorno x = 0 (Dirichlet)
T_initial = 20.0      # temperatura inicial (°C)

dx = L / (n - 1)
x = np.linspace(0, L, n)

# Verificação da condição CFL
cfl = abs(u) * dt / dx
print("CFL =", cfl)
if cfl > 1:
    print("⚠️ Violação da condição CFL! O método será instável.")

# 2. Condição inicial
T = np.ones(n) * T_initial

# Armazenar para visualização
tempos_plot = [0, 1, 2, 3, 5]
Ts = {0: T.copy()}

# 3. Loop no tempo (explícito)
t = 0.0
k = 0

while t < t_total:
    T_old = T.copy()

    for i in range(1, n):
        T[i] = T_old[i] - u * dt/dx * (T_old[i] - T_old[i-1])

    T[0] = TA          # Dirichlet em x=0
    T[-1] = T[-2]      # Neumann (derivada nula) em x=L

    if np.isclose(t, tempos_plot, atol=dt).any():
        Ts[round(t)] = T.copy()

    t += dt
    k += 1

Ts[5] = T.copy()

# 4. Plot dos resultados
plt.figure(figsize=(10,5))

for tp in tempos_plot:
    plt.plot(x, Ts[tp], label=f"t = {tp:.1f} s")

plt.xlabel("x (m)")
plt.ylabel("Temperatura (°C)")
plt.title("Equação de Advecção 1D - Método Explícito")
plt.grid(True)
plt.legend()
plt.show()
