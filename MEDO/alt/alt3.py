import numpy as np
import matplotlib.pyplot as plt

# Parâmetros físicos e geométricos
comprimento_barra = 1.0
difusividade_termica = 1.0e-4
temp_contorno_esquerda = 100.0
fluxo_contorno_direita = 0.0
temp_ambiente = 20.0

# Parâmetros de discretização espacial
num_pontos = 51
espaco_grid = comprimento_barra / (num_pontos - 1)
posicoes = np.linspace(0, comprimento_barra, num_pontos)

# Parâmetros temporais
passo_tempo = 10.0
tempo_simulacao = 500.0
num_passos_tempo = int(tempo_simulacao / passo_tempo) + 1

# Número de Fourier - governa a estabilidade do esquema numérico
r = difusividade_termica * passo_tempo / (espaco_grid**2)

# Inicialização do campo de temperatura com condição inicial uniforme
campo_temperatura = np.ones(num_pontos) * temp_ambiente
campo_temperatura[0] = temp_contorno_esquerda  # Aplica condição de contorno em x=0


def montar_sistema_matricial():
    """Constrói a matriz tridiagonal do sistema linear implícito"""
    # Diagonal principal: coeficiente do nó central
    diagonal_principal = np.ones(num_pontos) * (1 + 2*r)
    # Diagonal inferior: coeficiente do nó à esquerda
    diagonal_inferior = np.ones(num_pontos-1) * (-r)
    # Diagonal superior: coeficiente do nó à direita
    diagonal_superior = np.ones(num_pontos-1) * (-r)
    
    # Condição de contorno de Dirichlet em x=0
    diagonal_principal[0] = 1.0
    diagonal_superior[0] = 0.0
    
    # Condição de contorno de Neumann em x=L
    diagonal_principal[num_pontos-1] = 1 + r
    diagonal_inferior[num_pontos-2] = -r
    
    # Monta matriz tridiagonal completa
    matriz_completa = np.zeros((num_pontos, num_pontos))
    np.fill_diagonal(matriz_completa, diagonal_principal)
    np.fill_diagonal(matriz_completa[1:], diagonal_inferior)
    np.fill_diagonal(matriz_completa[:, 1:], diagonal_superior)
    
    return matriz_completa


def resolver_sistema_linear(matriz, vetor_b):
    """Resolve sistema Ax=b usando eliminação de Gauss com pivotamento parcial"""
    n = len(vetor_b)
    A = matriz.copy()
    b = vetor_b.copy()
    
    # Fase de eliminação
    for i in range(n):
        # Pivotamento parcial para estabilidade numérica
        max_linha = i + np.argmax(np.abs(A[i:, i]))
        if max_linha != i:
            A[[i, max_linha]] = A[[max_linha, i]]
            b[i], b[max_linha] = b[max_linha], b[i]
        
        # Eliminação dos elementos abaixo do pivô
        for j in range(i + 1, n):
            if A[i, i] != 0:
                fator = A[j, i] / A[i, i]
                A[j, i:] -= fator * A[i, i:]
                b[j] -= fator * b[i]
    
    # Fase de substituição retroativa
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
    
    return x


def executar_simulacao(pontos, intervalo_tempo, duracao=500.0):
    """Simula difusão de calor com diferentes refinamentos"""
    L_barra = 1.0
    coef_difusao = 1e-4
    temperatura_inicial = 20.0
    temperatura_esquerda = 100.0
    fluxo_direita = 0.0
    
    # Discretização espacial
    delta_x = L_barra / (pontos - 1)
    coordenadas = np.linspace(0, L_barra, pontos)
    r = coef_difusao * intervalo_tempo / (delta_x**2)
    
    # Montagem da matriz do sistema
    diag_princ = np.ones(pontos) * (1 + 2*r)
    diag_inf = np.ones(pontos-1) * (-r)
    diag_sup = np.ones(pontos-1) * (-r)
    
    # Condições de contorno
    diag_princ[0] = 1.0
    diag_sup[0] = 0.0
    diag_princ[-1] = 1 + r
    diag_inf[-1] = -r
    
    # Montagem da matriz completa
    matriz_sistema = np.zeros((pontos, pontos))
    np.fill_diagonal(matriz_sistema, diag_princ)
    np.fill_diagonal(matriz_sistema[1:], diag_inf)
    np.fill_diagonal(matriz_sistema[:, 1:], diag_sup)
    
    # Inicialização do campo de temperatura
    temperatura = np.ones(pontos) * temperatura_inicial
    temperatura[0] = temperatura_esquerda
    
    # Loop temporal - método implícito
    iteracoes = int(duracao / intervalo_tempo)
    for _ in range(iteracoes):
        vetor_rhs = temperatura.copy()
        vetor_rhs[0] = temperatura_esquerda

        vetor_rhs[-1] = temperatura[-1] + r * delta_x * fluxo_direita
        temperatura = resolver_sistema_linear(matriz_sistema, vetor_rhs)
    
    return coordenadas, temperatura

sistema_bandas = montar_sistema_matricial()

print("\nIniciando simulação temporal...")

# Loop temporal principal
for indice_tempo in range(1, num_passos_tempo):
    tempo_corrente = indice_tempo * passo_tempo
    
    # Constrói vetor do lado direito do sistema linear
    vetor_lado_direito = campo_temperatura.copy()
    vetor_lado_direito[0] = temp_contorno_esquerda
    # Implementa condição de Neumann em x=L
    vetor_lado_direito[num_pontos-1] = campo_temperatura[num_pontos-1] + r * espaco_grid * fluxo_contorno_direita
    
    # Resolve sistema linear para avançar no tempo
    campo_temperatura = resolver_sistema_linear(sistema_bandas, vetor_lado_direito)

print("\nSimulação concluída!")

# Gráfico 1: Solução com parâmetros padrão
print("\n" + "=" * 60)
print("SOLUÇÃO COM PARÂMETROS PADRÃO")
print("=" * 60)
print(f"Número de pontos: {num_pontos}")
print(f"Passo de tempo: {passo_tempo} s")
print(f"Tempo de simulação: {tempo_simulacao} s")
print(f"Temperatura em x = 0 m: {campo_temperatura[0]:.2f} °C")
print(f"Temperatura em x = {comprimento_barra/2} m: {campo_temperatura[num_pontos//2]:.2f} °C")
print(f"Temperatura em x = {comprimento_barra} m: {campo_temperatura[-1]:.2f} °C")
print(f"Temperatura média: {campo_temperatura.mean():.2f} °C")
print("=" * 60)

plt.figure(figsize=(10, 6))
plt.plot(posicoes, campo_temperatura, 'o-', linewidth=2, markersize=6, color='darkgreen')
plt.xlabel('Posição x (m)', fontsize=12)
plt.ylabel('Temperatura (°C)', fontsize=12)
plt.title(f'Distribuição de Temperatura em t = {tempo_simulacao} s\n(n = {num_pontos}, Δt = {passo_tempo} s)', 
          fontsize=13, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Estudo de convergência temporal com diferentes passos de tempo
num_pontos_temp = 101
lista_passos_tempo = [1.0, 2.0, 4.0, 8.0, 16.0, 32.0]
solucoes_convergencia_temporal = []

print("================= Análise de Convergência Temporal - Variando Δt =================")
for passo in lista_passos_tempo:
    coords, temp_final = executar_simulacao(num_pontos_temp, passo)
    solucoes_convergencia_temporal.append((passo, temp_final))
    print(f"Δt = {passo:5.1f} s | T(x=L) = {temp_final[-1]:.4f} °C")

# Gráfico de Convergência Temporal
plt.figure(figsize=(10, 6))
for passo, temp_final in solucoes_convergencia_temporal:
    plt.plot(coords, temp_final, marker='o', markersize=3, linewidth=1.5, label=f'Δt = {passo} s')
plt.xlabel('Posição x (m)', fontsize=12)
plt.ylabel('Temperatura (°C)', fontsize=12)
plt.title('Análise de convergência temporal', fontsize=13, fontweight='bold')
plt.legend(fontsize=9, loc='best')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Estudo de convergência espacial com diferentes números de pontos
passo_tempo_fixo = 1.0
lista_num_pontos = [10, 20, 40, 80, 160, 320]
solucoes_convergencia_espacial = []

print("================= Análise de Convergência Espacial - Variando Δx =================")

for n_pts in lista_num_pontos:
    coords_espacial, temp_final_espacial = executar_simulacao(n_pts, passo_tempo_fixo)
    delta_x = comprimento_barra / (n_pts - 1)
    solucoes_convergencia_espacial.append((delta_x, coords_espacial, temp_final_espacial))
    print(f"n = {n_pts:4d} pontos | Δx = {delta_x:.6f} m | T(x=L) = {temp_final_espacial[-1]:.6f} °C")

print("=" * 60)

# Gráfico de Convergência Espacial
plt.figure(figsize=(10, 6))
for delta_x, coords_espacial, temp_final_espacial in solucoes_convergencia_espacial:
    n_pts = len(coords_espacial)
    plt.plot(coords_espacial, temp_final_espacial, marker='o', markersize=3, 
             linewidth=1.5, label=f'n = {n_pts} (Δx = {delta_x:.4f} m)')
plt.xlabel('Posição x (m)', fontsize=12)
plt.ylabel('Temperatura (°C)', fontsize=12)
plt.title('Análise de convergência espacial', fontsize=13, fontweight='bold')
plt.legend(fontsize=9, loc='best')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()