import numpy as np
import matplotlib.pyplot as plt


def solver_diferencas_finitas(b, y_inicial, tol=1e-6, max_iter=10000):
    b = np.asarray(b, dtype=float)
    y = np.asarray(y_inicial, dtype=float)
    n = len(y)
    for k in range(max_iter):
        erro = 0.0
        for i in range(1, n - 1):
            aux = 0.5 * (b[i] + y[i - 1] + y[i + 1])
            erro = max(erro, abs(aux - y[i]))
            y[i] = aux
        if erro < tol:
            return y, k + 1
    print("Aviso: não convergiu em", max_iter, "iterações.")
    return y, max_iter


def momento_fletor(x, L, P):
    M = np.zeros_like(x)
    for i, xi in enumerate(x):
        if xi < L / 2:
            M[i] = (P / 2) * xi
        else:
            M[i] = (P / 2) * (L - xi)
    return M


def deflexao_viga(L=10.0, P=10000.0, E=200e9, I=5e-5, n=50):
    h = L / (n - 1)
    x = np.linspace(0, L, n)
    M = momento_fletor(x, L, P)

    b = (h**2 / (E * I)) * M
    b[0] = 0
    b[-1] = 0
    y_inicial = np.zeros(n)
    y_inicial[0] = 0
    y_inicial[-1] = 0
    y, it = solver_diferencas_finitas(b, y_inicial, tol=1e-6)
    print(f"Convergência em {it} iterações para n={n}")
    return x, -y  # inverte o sinal da deflexão


if __name__ == "__main__":
    # Parâmetros do problema
    L = 10.0
    P = 10000.0
    E = 200e9
    I = 5e-5

    for n in [5, 10, 20, 40, 80]:
      x, y = deflexao_viga(L, P, E, I, n)
      plt.figure(figsize=(6, 4))
      plt.plot(x, y, marker='o')
      plt.title('Deflexão da Viga (carga concentrada no centro) - n={}'.format(n))
      plt.xlabel('Posição ao longo da viga (m)')
      plt.ylabel('Deflexão (m)')
      plt.grid()
      plt.show()

    n_values = [5, 10, 20, 40, 80]
    fig, axs = plt.subplots(1, len(n_values), figsize=(18, 4))
    for ax, n in zip(axs, n_values):
        x, y = deflexao_viga(L, P, E, I, n)
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
        x, y = deflexao_viga(L, P, E, I, n)
        plt.plot(x, y, marker='o', label=f'n={n}')
    plt.title('Refinamento de Malha - Comparação das Deflexões')
    plt.xlabel('Posição ao longo da viga (m)')
    plt.ylabel('Deflexão (m)')
    plt.legend()
    plt.grid(True)
    plt.show()
