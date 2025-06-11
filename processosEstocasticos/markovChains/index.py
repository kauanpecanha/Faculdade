import numpy as np

# Número total de músicas
k = 4

# Estados: 0, 1, 2, 3, 4 (músicas distintas ouvidas)
# Matriz de transição P (5x5)
P = np.zeros((k, k))

P = np.array([
    [1/4, 3/4, 0, 0],
    [0, 2/4, 2/4, 0],
    [0, 0, 3/4, 1/4],
    [0, 0, 0, 1],
])

# Estado inicial: 0 músicas ouvidas
pi = np.zeros(k)
pi[0] = 1

# Evoluir a distribuição por 6 passos
for _ in range(6):
    print(pi)
    print(P)
    pi = pi @ P
    print("\n\n")
    print(pi)
    print("=================================================")

# Resultado: probabilidade de estar no estado 4 após 6 tocadas
print("\n\n")
print(pi[-1])
