
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
# coeficientes fornecidos
coeficientes = [
    (13.1, -13.94, 1.71),   
    (16.00, -13.94, 1.71),  
    (13.1, -17.00, 1.71),   
    (13.1, -13.94, 0.95),   
    (11.00, -12.0, 1.95),
]

labels = [
    "13.1g -13.94g²",
    "16.00g, -13.94g²",
    "13.1g, -17.00g²",
    "13.1g, -13.94g²",
    "11.00g, -12.0g²"
]

# Gráfico de G(t)
plt.figure(figsize=(7,5))
for idx, (a1, a2, b1) in enumerate(coeficientes):
    y0 = [G_init, F_init]
    result = solve_rk4(lambda vars: np.array([a1*vars[0] + a2*vars[0]**2, b1*vars[0]]), y0, t, h)
    plt.plot(t, result[:, 0], label=f"G - {labels[idx]}")
plt.title("Evolução de G(t)")
plt.xlabel("Tempo")
plt.ylabel("G")
plt.legend()
plt.show()

labels = [
    "13.1g -13.94g²",
    "16.00g, -13.94g²",
    "13.1g, -17.00g²",
    "13.1g, -13.94g²",
    "11.00g, -12.0g²"
]

# Gráfico de F(t)
plt.figure(figsize=(7,5))
for idx, (a1, a2, b1) in enumerate(coeficientes):
    y0 = [G_init, F_init]
    result = solve_rk4(lambda vars: np.array([a1*vars[0] + a2*vars[0]**2, b1*vars[0]]), y0, t, h)
    plt.plot(t, result[:, 1], label=f"F - {labels[idx]}")
plt.title("Evolução de F(t)")
plt.xlabel("Tempo")
plt.ylabel("F")
plt.legend()
plt.show()