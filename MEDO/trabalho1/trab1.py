
# importações
from rk4 import solve_rk4
import numpy as np
import matplotlib.pyplot as plt

# definição das EDOs

# G: concentração adimensional da massa das células.
def dG(G):
    return (
        13.1 * G - 13.94 * G**2
    )

# F: concentração adimensional de penicilina.
def dF(G):
    return (
        1.71 * G
    )

G_init = 0.03
F_init = 0.0

# vetor de valores de tempo
t = np.linspace(0, 1, 20)

# valor do passo
h = 0.05

# sistema de EDOs
def system(vars):
    G, F = vars
    return np.array([dG(G), dF(G)])

# vetor de condições iniciais
y0 = [G_init, F_init]

# ========================================== Implementação da Instrução 1 ==========================================

result = solve_rk4(system, y0, t, h)

# # Exemplo de plot
plt.plot(t, result[:, 0], label='G (Células)')
plt.plot(t, result[:, 1], label='F (Penicilina)')
plt.title('Gráfico de G e F')
plt.xlabel('Tempo')
plt.ylabel('Concentração adimensional')
plt.legend()
plt.show()

# ========================================== Implementação da Instrução 2 ==========================================

# Parâmetros para teste de convergência
hs = [0.05, 0.15, 0.20]
t_end = 1

plt.figure(figsize=(8, 5))
for h in hs:
    n_steps = int(t_end / h) + 1
    t = np.linspace(0, t_end, n_steps)
    y0 = [G_init, F_init]
    result = solve_rk4(system, y0, t, h)
    plt.plot(t, result[:, 0], label=f'G, h={h}')
    plt.plot(t, result[:, 1], '--', label=f'F, h={h}')

plt.xlabel('Tempo')
plt.ylabel('Concentração adimensional')
plt.legend()
plt.title('Teste de Convergência Numérica (RK4)')
plt.show()

# # ========================================== Implementação da Instrução 3 ==========================================

# Simulação principal com h = 0.05
tmax = 1
h = 0.05
n_steps = int(tmax / h) + 1
t = np.linspace(0, tmax, n_steps)
y0 = [G_init, F_init]
result = solve_rk4(system, y0, t, h)

# Exibir resultados em tabela
# print("t\tG\t\tF")
# for i in range(n_steps):
#     print(f"{t[i]:.2f}\t{result[i,0]:.6f}\t{result[i,1]:.6f}")
    
# ========================================== Implementação da Instrução 4 ==========================================

coeficientes = [
    (13.1, -13.94, 1.71),      # valores originais
    (15.0, -13.94, 1.71),      # variação em a1
    (13.1, -15.0, 1.71),       # variação em a2
    (13.1, -13.94, 2.0),       # variação em b1
    (12.0, -12.0, 1.5),        # variação em todos
]

labels = [
    "(13.1, -13.94, 1.71)",
    "(15.0, -13.94, 1.71)",
    "(13.1, -15.0, 1.71)",
    "(13.1, -13.94, 2.0)",
    "(12.0, -12.0, 1.5)"
]

plt.figure(figsize=(8, 5))
for idx, (a1, a2, b1) in enumerate(coeficientes):
    def dG(G):
        return a1 * G + a2 * G**2
    def dF(G):
        return b1 * G
    def system(vars):
        G, F = vars
        return np.array([dG(G), dF(G)])
    y0 = [G_init, F_init]
    result = solve_rk4(system, y0, t, h)
    if(idx == 0):
        plt.plot(t, result[:, 0], label=f'G/F - {labels[idx]}')
    else:
        plt.plot(t, result[:, 0], '--', label=f'G/F - {labels[idx]}')

plt.xlabel('Tempo')
plt.ylabel('Concentração adimensional de G')
plt.legend()
plt.title('Análise de Sensibilidade dos Coeficientes')
plt.grid(True)
plt.tight_layout()
plt.show()