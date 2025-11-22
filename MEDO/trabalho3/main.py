import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve_banded

# PARÂMETROS DO PROBLEMA (4.1)
# Comprimento da barra (m)
L = 1.0
# Coeficiente de difusão térmica (m²/s)
alpha = 1.0e-4             
# Número de nós no espaço
n = 51                     
# Passo de tempo (s)
dt = 10.0                  
# Tempo total de simulação (s)
t_total = 500.0            
# Temperatura inicial (°C)
T_inicial = 20.0           
# Temperatura em x=0 (°C)
T_A = 100.0                
# Fluxo de calor em x=L (°C/m)
q_L = 0.0                  

# DISCRETIZAÇÃO
# Espaçamento espacial
dx = L / (n - 1)           
# Vetor de posições
x = np.linspace(0, L, n)
# Número de passos de tempo
n_steps = int(t_total / dt) + 1  

# Parâmetro adimensional
r = alpha * dt / (dx**2)

print("=" * 60)
print("SIMULAÇÃO DE DIFUSÃO DE CALOR - MÉTODO IMPLÍCITO")
print("=" * 60)
print(f"Comprimento da barra: {L} m")
print(f"Coeficiente de difusão: {alpha} m²/s")
print(f"Número de nós: {n}")
print(f"Δx = {dx:.6f} m")
print(f"Δt = {dt} s")
print(f"Número de passos de tempo: {n_steps}")
print(f"Parâmetro r = α·Δt/Δx² = {r:.6f}")
print("=" * 60)

# CONDIÇÃO INICIAL (4.2)
T = np.ones(n) * T_inicial
T[0] = T_A  # Condição de contorno em x=0

# Armazenar soluções para plotagem
tempos_plot = [0, 50, 100, 200, 300, 500]
T_historico = {}
T_historico[0] = T.copy()

def construir_matriz_sistema():
    """
    Constrói a matriz A do sistema AT^{k+1} = b^k
    Retorna no formato banded (diagonal_superior, diagonal_principal, diagonal_inferior)
    """
    # Diagonal principal
    diag_main = np.ones(n) * (1 + 2*r)
    # Diagonal inferior
    diag_lower = np.ones(n-1) * (-r)
    # Diagonal superior
    diag_upper = np.ones(n-1) * (-r)
    
    # Condição de contorno de Dirichlet em x=0 (i=0) (4.4)
    diag_main[0] = 1.0
    diag_upper[0] = 0.0
    
    # Condição de contorno de Neumann em x=L (i=n-1) (4.4)
    diag_main[n-1] = 1 + r
    diag_lower[n-2] = -r
    
    ab = np.zeros((3, n))
    ab[0, 1:] = diag_upper   # Diagonal superior 
    ab[1, :] = diag_main     # Diagonal principal
    ab[2, :-1] = diag_lower  # Diagonal inferior 
    
    return ab

def simular_difusao(n, dt, t_total=500.0):
    """
    Executa a simulação e retorna o vetor de temperatura final.
    """
    L = 1.0
    alpha = 1e-4
    T_inicial = 20.0
    T_A = 100.0
    q_L = 0.0
    
    dx = L / (n - 1)
    x = np.linspace(0, L, n)
    r = alpha * dt / (dx**2)
    
    # Matriz
    diag_main = np.ones(n) * (1 + 2*r)
    diag_lower = np.ones(n-1) * (-r)
    diag_upper = np.ones(n-1) * (-r)
    diag_main[0] = 1.0
    diag_upper[0] = 0.0
    diag_main[-1] = 1 + r
    diag_lower[-1] = -r
    
    ab = np.zeros((3, n))
    ab[0, 1:] = diag_upper
    ab[1, :] = diag_main
    ab[2, :-1] = diag_lower
    
    T = np.ones(n) * T_inicial
    T[0] = T_A
    
    n_steps = int(t_total / dt)
    for _ in range(n_steps):
        b = T.copy()
        b[0] = T_A
        b[-1] = T[-1] + r * dx * q_L
        T = solve_banded((1, 1), ab, b)
    
    return x, T

# Construir matriz (4.3)
A_banded = construir_matriz_sistema()

for k in range(1, n_steps): # (4.5)
    t_atual = k * dt
    
    # Construir vetor do lado direito b^k
    b = T.copy()
    
    # Condição de contorno de Dirichlet em x=0
    b[0] = T_A
    
    # Condição de contorno de Neumann em x=L
    b[n-1] = T[n-1] + r * dx * q_L
    
    # Resolver sistema linear AT^{k+1} = b^k
    T = solve_banded((1, 1), A_banded, b)
    
    # Armazenar resultados nos tempos desejados
    if t_atual in tempos_plot:
        T_historico[t_atual] = T.copy()
        print(f"t = {t_atual:6.1f} s | T_min = {T.min():6.2f}°C | T_max = {T.max():6.2f}°C")

# Gráfico 1: Evolução temporal da temperatura em diferentes instantes
print("SOLUÇÃO COM PARÂMETROS PADRÃO")
plt.figure(figsize=(10, 6))
for t in sorted(T_historico.keys()):
    plt.plot(x, T_historico[t], label=f't = {t} s', linewidth=2)
plt.xlabel('Posição x (m)', fontsize=12)
plt.ylabel('Temperatura (°C)', fontsize=12)
plt.title('Distribuição de Temperatura ao Longo da Barra', fontsize=13, fontweight='bold')
plt.legend(fontsize=9)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("=" * 60)

# ANÁLISE DE CONVERGÊNCIA TEMPORAL
n = 101
dt_values = [1.0, 2.5, 5.0, 10.0, 25.0, 50.0]
T_solucoes_dt = []

print("ANÁLISE DE CONVERGÊNCIA TEMPORAL - Variando Δt")
for dt in dt_values:
    x_temp, T_final = simular_difusao(n, dt)
    T_solucoes_dt.append((dt, T_final))
    print(f"Δt = {dt:5.1f} s | T(x=L) = {T_final[-1]:.4f} °C")

print("=" * 60)

# Gráfico 2: Convergência Temporal
plt.figure(figsize=(10, 6))
for (dt, T_final) in T_solucoes_dt:
    plt.plot(x_temp, T_final, marker='o', markersize=3, linewidth=1.5, label=f'Δt = {dt:.1f} s')
plt.xlabel('Posição x (m)', fontsize=12)
plt.ylabel('Temperatura (°C)', fontsize=12)
plt.title('Convergência Temporal - Diferentes Δt', fontsize=13, fontweight='bold')
plt.legend(fontsize=9, loc='best')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ANÁLISE DE CONVERGÊNCIA ESPACIAL
dt_fixo = 1.0
n_values = [11, 21, 41, 81, 161, 321]
T_solucoes_n = []

print("ANÁLISE DE CONVERGÊNCIA ESPACIAL - Variando Δx")
for n_pts in n_values:
    x_espacial, T_final_espacial = simular_difusao(n_pts, dt_fixo)
    dx_espacial = L / (n_pts - 1)
    T_solucoes_n.append((dx_espacial, x_espacial, T_final_espacial))
    print(f"n = {n_pts:4d} pontos | Δx = {dx_espacial:.6f} m | T(x=L) = {T_final_espacial[-1]:.6f} °C")

print("=" * 60)

# Gráfico 3: Convergência Espacial
plt.figure(figsize=(10, 6))
for (dx_espacial, x_espacial, T_final_espacial) in T_solucoes_n:
    n_pts = len(x_espacial)
    plt.plot(x_espacial, T_final_espacial, marker='o', markersize=3, 
             linewidth=1.5, label=f'n = {n_pts} (Δx = {dx_espacial:.4f} m)')
plt.xlabel('Posição x (m)', fontsize=12)
plt.ylabel('Temperatura (°C)', fontsize=12)
plt.title('Convergência Espacial - Diferentes Δx', fontsize=13, fontweight='bold')
plt.legend(fontsize=9, loc='best')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()