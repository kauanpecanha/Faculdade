
# bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from scipy.linalg import eigh

# casos
L1 = lambda x: np.ones_like(x) # Constante
L2 = lambda x: 1 + x # Linear
L3 = lambda x: 1 + 4 * (x - 0.5)**2 # Parabólica

casos = {
    "Constante": L1,
    "Linear": L2,
    "Parabólica": L3
}

def solve_psl_circuit(N, l_func):
    """modelo com PSL (Sturm-Liouville)

    Args:
        N (int): número de pontos
        l_func (function): função que define o perfil L(x)

    Returns:
        float: resultados do modelo com PSL
    """
    h = 1 / (N + 1)
    x_full = np.linspace(0, 1, N + 2)
    x_mid = (x_full[:-1] + x_full[1:]) / 2

    L_vals = l_func(x_mid)
    p_vals = 1 / L_vals
    C_vals = np.ones(N)

    A = np.zeros((N, N))
    for i in range(N):
        A[i, i] = (p_vals[i] + p_vals[i+1]) / h**2
        if i > 0:
            A[i, i-1] = -p_vals[i] / h**2
        if i < N - 1:
            A[i, i+1] = -p_vals[i+1] / h**2

    W = np.diag(C_vals)
    lambdas, eigvecs = eigh(A, W)
    omegas = np.sqrt(lambdas[:5])
    modos = eigvecs[:, :5]
    return x_full, omegas, modos


def solve_hom_circuit(N):
    """modelo homogeneo (sem PSL)

    Args:
        N (int): numero de pontos

    Returns:
        float: resultados do modelo homogeneo
    """
    h = 1 / (N + 1)
    x_full = np.linspace(0, 1, N + 2)
    main_diag = 2 * np.ones(N)
    off_diag = -1 * np.ones(N - 1)
    A = (np.diag(main_diag) + np.diag(off_diag, k=1) + np.diag(off_diag, k=-1)) / h**2
    B = np.identity(N)
    lambdas, eigvecs = eigh(A, B)
    omegas = np.sqrt(lambdas[:5])
    modos = eigvecs[:, :5]
    return x_full, omegas, modos

# ----------------------------
# Execução para N pontos
# ----------------------------
N = 1000
x_full, omega_homog, modos_homog = solve_hom_circuit(N)

resultados = {}
for nome, Lfun in casos.items():
    x_full, omegas, modos = solve_psl_circuit(N, Lfun)
    resultados[nome] = {"x": x_full, "ω": omegas, "modos": modos}

# plot dos dados
for nome, dados in resultados.items():
    plt.figure(figsize=(12, 6))
    for i in range(3):
        y_psl = np.zeros(N + 2)
        y_std = np.zeros(N + 2)
        y_psl[1:-1] = dados["modos"][:, i]
        y_std[1:-1] = modos_homog[:, i]

        plt.subplot(1, 3, i+1)
        plt.plot(x_full, y_std, '--', label=f'Sem PSL (ω={omega_homog[i]:.2f})', alpha=0.7)
        plt.plot(x_full, y_psl, '-', label=f'Com PSL (ω={dados["ω"][i]:.2f})', alpha=0.7)

        plt.title(f'{nome}: Modo {i+1}')
        plt.xlabel('x')
        plt.grid(True)
        if i == 0:
            plt.ylabel('Tensão y(x)')
        plt.legend()
    plt.suptitle(f'Modos Naturais - {nome}')
    plt.tight_layout()
    plt.show()

# tabela comparativa das frequências
tabelas = []
for nome, dados in resultados.items():
    df = pd.DataFrame({
        'Modo': [f'{i+1}' for i in range(5)],
        'ω (com PSL)': dados["ω"],
        'ω (sem PSL)': omega_homog,
        'Δω (%)': 100 * (omega_homog - dados["ω"]) / omega_homog
    })
    df["Perfil L(x)"] = nome
    tabelas.append(df)

tabela_final = pd.concat(tabelas, ignore_index=True)
print("Comparação das Frequências Naturais para cada perfil de L(x):")
print(tabela_final.to_string(index=False))
