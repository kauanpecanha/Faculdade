import numpy as np
import matplotlib.pyplot as plt


L = 10.0               # comprimento da viga (m)
P = 10e4               # carga concentrada no centro (N)
E = 2e11               # módulo de elasticidade (Pa)
I = 5e-5               # momento de inércia (m^4)
EI = E * I             # rigidez à flexão


def M(x, L, P):
    if x < L/2:
        return (P/2) * x
    else:
        return (P/2) * (L - x)


def resolver_deflexao(L, P, EI, n):
    dx = L / (n - 1)       
    A = np.zeros((n, n))
    b = np.zeros(n)

    for i in range(n):
        if i == 0:
            A[i, i] = 1   
        elif i == n-1:
            A[i, i] = 1   
        else:
            A[i, i-1] = 1
            A[i, i]   = -2
            A[i, i+1] = 1
            xi = i * dx
            b[i] = (M(xi, L, P) * dx**2) / EI

    y = np.linalg.solve(A, b)
    x = np.linspace(0, L, n)
    return x, y


# Solução com n=5
x, y = resolver_deflexao(L, P, EI, n=5)
plt.plot(x, y, marker='o')
plt.title('Deflexão da Viga (carga concentrada no centro)')
plt.xlabel('Posição ao longo da viga (m)')
plt.ylabel('Deflexão (m)')
plt.grid()
plt.show()

# Estudo de refinamento de malha
n_values = [5, 10, 20, 50, 100]

fig, axs = plt.subplots(1, len(n_values), figsize=(18, 4))  # uma linha, várias colunas
for ax, n in zip(axs, n_values):
    x, y = resolver_deflexao(L, P, EI, n)
    ax.plot(x, y, marker='o', label=f'n={n}')
    ax.set_title(f'n = {n}')
    ax.set_xlabel('Posição (m)')
    ax.set_ylabel('Deflexão (m)')
    ax.grid(True)
    ax.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
for n in n_values:
    x, y = resolver_deflexao(L, P, EI, n)
    plt.plot(x, y, marker='o', label=f'n={n}')
plt.title('Refinamento de Malha')
plt.xlabel('Posição ao longo da viga (m)')
plt.ylabel('Deflexão (m)')
plt.legend()
plt.grid(True)
plt.show()

# Estudo da variação de P
P_values = [500, 1000, 2000]

fig, axs = plt.subplots(1, len(P_values), figsize=(15, 4))
for ax, P in zip(axs, P_values):
    x, y = resolver_deflexao(L, P, EI, n=50)
    ax.plot(x, y, marker='o', label=f'P={P} N')
    ax.set_title(f'P = {P} N')
    ax.set_xlabel('Posição (m)')
    ax.set_ylabel('Deflexão (m)')
    ax.grid(True)
    ax.legend()

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
for P in P_values:
    x, y = resolver_deflexao(L, P, EI, n=50)
    plt.plot(x, y, marker='o', label=f'P={P} N')
plt.title('Deflexão para diferentes cargas P')
plt.xlabel('Posição ao longo da viga (m)')
plt.ylabel('Deflexão (m)')
plt.legend()
plt.grid(True)
plt.show()

# Estudo da variação de EI
EI_values = [EI/2, EI, EI*2]
fig, axs = plt.subplots(1, len(EI_values), figsize=(15, 4))

for ax, EI_val in zip(axs, EI_values):
    x, y = resolver_deflexao(L, P, EI_val, n=50)
    ax.plot(x, y, marker='o', label=f'EI={EI_val:.1e}')
    ax.set_title(f'EI = {EI_val:.1e}')
    ax.set_xlabel('Posição (m)')
    ax.set_ylabel('Deflexão (m)')
    ax.grid(True)
    ax.legend()

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
for EI_val in EI_values:
    x, y = resolver_deflexao(L, P, EI_val, n=50)
    plt.plot(x, y, marker='o', label=f'EI={EI_val:.1e}')
plt.title('Deflexão para diferentes rigidezes EI')
plt.xlabel('Posição ao longo da viga (m)')
plt.ylabel('Deflexão (m)')
plt.legend()
plt.grid(True)
plt.show()
