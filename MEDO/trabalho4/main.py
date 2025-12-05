import numpy as np
import matplotlib.pyplot as plt

def calculate_temperature(T_old, u, dt, dx, n):
    T = T_old.copy()
    for i in range(1, n):
        T[i] = T_old[i] - u * dt/dx * (T_old[i] - T_old[i-1])
    return T

def simulate_advection(u, dx, dt, n, t_total, TA, T_initial):
    T = np.ones(n) * T_initial
    t = 0.0
    Ts = {0: T.copy()}

    while t < t_total:
        T_old = T.copy()
        T = calculate_temperature(T_old, u, dt, dx, n)

        # Condições de contorno
        T[0] = TA
        T[-1] = T[-2]
        
        if np.isclose(t, tempos_plot, atol=dt).any():
            Ts[round(t)] = T.copy()

        t += dt
    
    Ts[5] = T.copy()

    return Ts

# 4.1. Parâmetros do problema
# comprimento da barra (m)
L = 1.0
# velocidade de advecção (m/s)
u = 0.1
# número de nós
n = 101
# passo de tempo (s)
dt = 0.05
# tempo total (s)
t_total = 5.0
# contorno x = 0 (Dirichlet)
TA = 100.0
# temperatura inicial (°C)
T_initial = 20.0

dx = L / (n - 1)
x = np.linspace(0, L, n)

# Verificação da condição CFL
cfl = abs(u) * dt / dx
print("CFL =", cfl)
if cfl > 1:
    print("Violação da condição CFL! O método será instável.")

# 4.2. Condição inicial
T = np.ones(n) * T_initial

# Armazenar para visualização
tempos_plot = [0, 1, 2, 3, 5]
Ts = {0: T.copy()}

# 4.3. Encontrando a solução numérica usando o método explícito
t = 0.0
k = 0
Ts = simulate_advection(u, dx, dt, n, t_total, TA, T_initial)

# 4.5. Plot dos resultados
plt.figure(figsize=(10,5))
for tp in tempos_plot:
    plt.plot(x, Ts[tp], label=f"t = {tp:.1f} s")
plt.xlabel("x (m)")
plt.ylabel("Temperatura (°C)")
plt.title("Equação de Advecção 1D - Método Explícito")
plt.grid(True)
plt.legend()
plt.show()

# 4.6. Estudo de Estabilidade
dt_values = [0.01, 0.02, 0.03, 0.04]
dx_values = [0.1, 0.05, 0.02, 0.01]
u_values = [0.05, 0.1, 0.15, 0.2]

# Variação de valores de passo de tempo
for dt in dt_values:
    Ts = simulate_advection(u, dx, dt, n, t_total, TA, T_initial)
    plt.figure(figsize=(10,5))
    for tp in tempos_plot:
        plt.plot(np.linspace(0, L, n), Ts[tp], label=f"t = {tp:.1f} s")
    plt.xlabel("x (m)")
    plt.ylabel("Temperatura (°C)")
    plt.title(f"Análise de Convergência (tempo) - Advecção 1D - dx = {dx}, dt = {dt}")
    plt.grid(True)
    plt.legend()
    plt.show()


# Variação de valores de passo de espaço
for dx in dx_values:
    Ts = simulate_advection(u, dx, dt, n, t_total, TA, T_initial)
    plt.figure(figsize=(10,5))
    for tp in tempos_plot:
        plt.plot(np.linspace(0, L, n), Ts[tp], label=f"t = {tp:.1f} s")
    plt.xlabel("x (m)")
    plt.ylabel("Temperatura (°C)")
    plt.title(f"Análise de convergência (espaço) Advecção 1D - dx = {dx}, dt = {dt}")
    plt.grid(True)
    plt.legend()
    plt.show()

# Variação de valores de velocidade de advecção
for u in u_values:
    Ts = simulate_advection(u, dx, dt, n, t_total, TA, T_initial)
    plt.figure(figsize=(10,5))
    for tp in tempos_plot:
        plt.plot(np.linspace(0, L, n), Ts[tp], label=f"t = {tp:.1f} s")
    plt.xlabel("x (m)")
    plt.ylabel("Temperatura (°C)")
    plt.title(f"Análise de Convergência (velocidade) Advecção 1D - u = {u}, dt = {dt}")
    plt.grid(True)
    plt.legend()
    plt.show()
