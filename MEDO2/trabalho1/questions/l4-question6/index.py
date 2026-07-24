from pathlib import Path

import matplotlib
import numpy as np

# Permite executar o programa em ambientes sem interface gráfica.
matplotlib.use("Agg")
import matplotlib.pyplot as plt


PASTA_SAIDA = Path(__file__).resolve().parents[2] / "figures"
PASTA_SAIDA.mkdir(parents=True, exist_ok=True)

U_ESQUERDA = -2.0
U_DIREITA = 0.0


def solucao_entropica(x, t):
    """Solução de rarefação do problema de Riemann para t > 0."""
    x = np.asarray(x, dtype=float)
    if t <= 0:
        return np.where(x <= 0, U_ESQUERDA, U_DIREITA)

    xi = x / t
    return np.where(
        xi <= U_ESQUERDA,
        U_ESQUERDA,
        np.where(xi >= U_DIREITA, U_DIREITA, xi),
    )


def gerar_diagrama_caracteristicas():
    """Gera o diagrama no plano (x,t), incluindo o leque de rarefação."""
    t = np.linspace(0, 3, 400)
    fig, ax = plt.subplots(figsize=(9, 6))

    # Características da região constante à esquerda: x = x0 - 2t.
    for x0 in np.linspace(-4, -0.4, 10):
        ax.plot(x0 + U_ESQUERDA * t, t, color="#1f77b4", lw=1.2)

    # Características da região constante à direita: x = x0.
    for x0 in np.linspace(0.4, 4, 10):
        ax.plot(x0 + U_DIREITA * t, t, color="#d62728", lw=1.2)

    # No leque, x/t = xi, com -2 <= xi <= 0.
    for xi in np.linspace(U_ESQUERDA, U_DIREITA, 17):
        ax.plot(xi * t, t, color="#2ca02c", lw=1.0, alpha=0.85)

    # Caminho que teria um choque de Rankine--Hugoniot (não entrópico).
    velocidade_rh = (0.5 * U_DIREITA**2 - 0.5 * U_ESQUERDA**2) / (
        U_DIREITA - U_ESQUERDA
    )
    ax.plot(
        velocidade_rh * t,
        t,
        "k--",
        lw=2,
        label=r"$x_s(t)=-t$ (choque não entrópico)",
    )

    ax.plot([], [], color="#2ca02c", label="leque de rarefação")
    ax.set(xlabel="x", ylabel="t", title="Diagrama de características")
    ax.set_xlim(-7, 4.5)
    ax.set_ylim(0, 3)
    ax.grid(alpha=0.25)
    ax.legend(loc="upper right")
    fig.tight_layout()
    fig.savefig(
        PASTA_SAIDA / "06_caracteristicas_rarefacao.png",
        dpi=300,
        bbox_inches="tight",
    )
    plt.close(fig)


def gerar_perfis():
    """Gera perfis da solução entrópica em diferentes instantes."""
    x = np.linspace(-7, 3, 1200)
    tempos = [0, 0.5, 1, 2, 3]
    fig, ax = plt.subplots(figsize=(9, 6))

    for t in tempos:
        ax.plot(x, solucao_entropica(x, t), lw=2, label=f"t = {t:g}")

    ax.set(
        xlabel="x",
        ylabel=r"$u(x,t)$",
        title="Solução entrópica: leque de rarefação",
    )
    ax.set_ylim(-2.2, 0.2)
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(
        PASTA_SAIDA / "07_perfis_rarefacao.png",
        dpi=300,
        bbox_inches="tight",
    )
    plt.close(fig)


def main():
    gerar_diagrama_caracteristicas()
    gerar_perfis()
    print(f"Gráficos salvos em: {PASTA_SAIDA}")


if __name__ == "__main__":
    main()
