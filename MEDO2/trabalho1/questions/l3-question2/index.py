import numpy as np
import matplotlib

# Permite executar o código em ambientes sem interface gráfica.
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from pathlib import Path


# Configurações gerais
PASTA_SAIDA = Path("../../figures")
PASTA_SAIDA.mkdir(parents=True, exist_ok=True)

VELOCIDADE = 2.0


# Condição inicial e solução
def u0(x):
    """
    Condição inicial:
        u(x, 0) = exp(-x²)
    """
    return np.exp(-(x ** 2))


def u(x, t, c=VELOCIDADE):
    """
    Solução da equação de transporte:
        u_t + c u_x = 0

    com condição inicial:
        u(x, 0) = exp(-x²)

    Solução:
        u(x, t) = exp(-(x - ct)²)
    """
    return u0(x - c * t)


# Figura 1: perfis da solução em diferentes instantes
def gerar_perfis():
    x = np.linspace(-10, 15, 1000)
    tempos = [0, 1, 2, 3, 4]

    plt.figure(figsize=(10, 6))

    for t in tempos:
        plt.plot(
            x,
            u(x, t),
            linewidth=2,
            label=f"t = {t}"
        )

    plt.xlabel("x")
    plt.ylabel("u(x,t)")
    plt.title("Solução da equação de transporte para diferentes tempos")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()

    caminho = PASTA_SAIDA / "03_solucao_questao2.png"
    plt.savefig(caminho, dpi=300, bbox_inches="tight")
    plt.close()

    print(f"Figura salva em: {caminho}")


# Figura 2: curvas características
def gerar_caracteristicas():
    x0_valores = np.linspace(-8, 8, 17)
    t = np.linspace(0, 5, 300)

    plt.figure(figsize=(10, 6))

    for x0 in x0_valores:
        x_caracteristica = x0 + VELOCIDADE * t

        plt.plot(
            x_caracteristica,
            t,
            linewidth=1.5
        )

    plt.xlabel("x")
    plt.ylabel("t")
    plt.title(
        f"Curvas características para velocidade constante c = {VELOCIDADE:g}"
    )
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    caminho = PASTA_SAIDA / "04_caracteristicas_questao2.png"
    plt.savefig(caminho, dpi=300, bbox_inches="tight")
    plt.close()

    print(f"Figura salva em: {caminho}")


# Figura 3: superfície tridimensional
def gerar_superficie():
    x = np.linspace(-10, 15, 300)
    t = np.linspace(0, 5, 200)

    X, T = np.meshgrid(x, t)
    U = u(X, T)

    fig = plt.figure(figsize=(11, 7))
    ax = fig.add_subplot(111, projection="3d")

    superficie = ax.plot_surface(
        X,
        T,
        U,
        cmap="viridis",
        edgecolor="none"
    )

    ax.set_xlabel("x")
    ax.set_ylabel("t")
    ax.set_zlabel("u(x,t)")
    ax.set_title("Representação tridimensional da solução")

    fig.colorbar(
        superficie,
        ax=ax,
        shrink=0.7,
        pad=0.1,
        label="u(x,t)"
    )

    plt.tight_layout()

    caminho = PASTA_SAIDA / "05_superficie_questao2.png"
    plt.savefig(caminho, dpi=300, bbox_inches="tight")
    plt.close()

    print(f"Figura salva em: {caminho}")


# Execução
def main():
    gerar_perfis()
    gerar_caracteristicas()
    gerar_superficie()

    print("\nTodas as figuras foram geradas com sucesso.")


if __name__ == "__main__":
    main()