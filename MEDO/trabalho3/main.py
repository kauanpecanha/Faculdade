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

# MONTAGEM DA MATRIZ TRIDIAGONAL
# Para sistema tridiagonal: -r·T_{i-1} + (1+2r)·T_i - r·T_{i+1} = T_i^k
# Usando formato banded do scipy para eficiência

def construir_matriz_sistema():
    """
    Constrói a matriz A do sistema AT^{k+1} = b^k
    Retorna no formato banded para scipy
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
    # Aproximação: (T_n - T_{n-1})/dx = q_L
    # Usando diferença backward implícita no nó fantasma
    # Equação: -r·T_{n-2} + (1+2r)·T_{n-1} - r·T_n = T_{n-1}^k
    # Com T_n = T_{n-1} + dx·q_L (nó fantasma)
    # Resulta em: -r·T_{n-2} + (1+r)·T_{n-1} = T_{n-1}^k + r·dx·q_L
    diag_main[n-1] = 1 + r
    diag_lower[n-2] = -r
    
    # Formato banded: [diagonal_superior, diagonal_principal, diagonal_inferior]
    ab = np.zeros((3, n))
    ab[0, 1:] = diag_upper   # Diagonal superior 
    ab[1, :] = diag_main     # Diagonal principal
    ab[2, :-1] = diag_lower  # Diagonal inferior 
    
    return ab

# Construir matriz (4.3)
A_banded = construir_matriz_sistema()


print("\nIniciando simulação temporal...")

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

print("\nSimulação concluída!")


# Gráfico 1: Evolução temporal da temperatura
# plt.subplot(2, 2, 1)
for t in sorted(T_historico.keys()):
    plt.plot(x, T_historico[t], label=f't = {t} s', linewidth=2)
plt.xlabel('Posição x (m)', fontsize=11)
plt.ylabel('Temperatura (°C)', fontsize=11)
plt.title('Distribuição de Temperatura ao Longo da Barra', fontsize=12, fontweight='bold')
plt.legend(fontsize=9)
plt.grid(True, alpha=0.3)
plt.show()

print("\n" + "=" * 60)
print("RESULTADOS FINAIS (t = {} s)".format(t_total))
print("=" * 60)
print(f"Temperatura em x = 0 m: {T[0]:.2f} °C")
print(f"Temperatura em x = {L/2} m: {T[n//2]:.2f} °C")
print(f"Temperatura em x = {L} m: {T[-1]:.2f} °C")
print(f"Temperatura média: {T.mean():.2f} °C")
print(f"Gradiente em x = L: {(T[-1] - T[-2])/dx:.6f} °C/m")
print("=" * 60)