import numpy as np
import matplotlib.pyplot as plt

# Variáveis Globais
L = 1.0
vel = 0.1
num_nos = 101
delta_t = 0.05
tempo_final = 5.0
T_esq = 100.0
T0 = 20.0

delta_x = L / (num_nos - 1)
xs = np.linspace(0, L, num_nos)
tempos_graf = [0, 1, 2, 3, 5]


# Funções
def atualiza_temp(Tprev, vel, dt, dx, n):
    Tnew = Tprev.copy()
    for j in range(1, n):
        Tnew[j] = Tprev[j] - vel * dt/dx * (Tprev[j] - Tprev[j-1])
    return Tnew

def executa_simulacao(vel, dx, dt, n, tmax, T_left, T_init):
    T = np.ones(n) * T_init
    tempo = 0.0
    resultados = {0: T.copy()}

    while tempo < tmax:
        hold = T.copy()
        T = atualiza_temp(hold, vel, dt, dx, n)

        T[0] = T_left
        T[-1] = T[-2]

        if np.isclose(tempo, tempos_graf, atol=dt).any():
            resultados[round(tempo)] = T.copy()

        tempo += dt

    resultados[5] = T.copy()
    return resultados

def condicao_cfl(vel, dt, dx):
    return abs(vel) * dt / dx


# Execução
T_ini = np.ones(num_nos) * T0
solucoes = executa_simulacao(vel, delta_x, delta_t, num_nos, tempo_final, T_esq, T0)

for tt in tempos_graf:
    plt.plot(xs, solucoes[tt], label=f"t = {tt} s")
plt.xlabel("x (m)")
plt.ylabel("Temperatura (°C)")
plt.title(f"Distribuição de Temperatura - dx = {delta_x:.4f}, dt = {delta_t:.4f}, CFL={condicao_cfl(vel, delta_t, delta_x):.2f}")
plt.legend()
plt.show()

# 4.6. Estudo de Estabilidade

# CFL < 1, CFL = 1, CFL > 1
lista_dt = [0.1, 0.2]
lista_dx = [0.005, 0.002]
lista_vel = [0.2, 1.0]

# Variação de passo de tempo
for dt in lista_dt:
    sol = executa_simulacao(vel, delta_x, dt, num_nos, tempo_final, T_esq, T0)
    for tt in tempos_graf:
        plt.plot(np.linspace(0, L, num_nos), sol[tt], label=f"t = {tt} s")
    plt.xlabel("x (m)")
    plt.ylabel("Temperatura (°C)")
    plt.title(f"Estabilidade (variação dt) - dx = {delta_x}, dt = {dt}, CFL={condicao_cfl(vel, dt, delta_x):.2f}")
    plt.legend()
    plt.show()

# Variação de passo de espaço
dt = 0.05
vel = 0.1
for dx in lista_dx:
    sol = executa_simulacao(vel, dx, dt, num_nos, tempo_final, T_esq, T0)
    for tt in tempos_graf:
        plt.plot(np.linspace(0, L, num_nos), sol[tt], label=f"t = {tt} s")
    plt.xlabel("x (m)")
    plt.ylabel("Temperatura (°C)")
    plt.title(f"Estabilidade (variação dx) - dx = {dx}, dt = {dt}, CFL={condicao_cfl(vel, dt, dx):.2f}")
    plt.legend()
    plt.show()

# Variação da velocidade de advecção
dt = 0.05
dx = 0.01
for vel in lista_vel:
    sol = executa_simulacao(vel, dx, dt, num_nos, tempo_final, T_esq, T0)
    for tt in tempos_graf:
        plt.plot(np.linspace(0, L, num_nos), sol[tt], label=f"t = {tt} s")
    plt.xlabel("x (m)")
    plt.ylabel("Temperatura (°C)")
    plt.title(f"Convergência (velocidade) - u = {vel}, dt = {dt}, dx = {dx}, CFL={condicao_cfl(vel, dt, dx):.2f}")
    plt.legend()
    plt.show()