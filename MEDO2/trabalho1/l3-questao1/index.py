import os
import numpy as np
import matplotlib.pyplot as plt

def u(x: np.ndarray, t: float | np.ndarray) -> np.ndarray:
    """
    Solução exata da EDP:

        u_t + 3u_x = 1
        u(x, 0) = x²

    Solução:
        u(x,t) = (x - 3t)² + t
    """
    return (x - 3 * t) ** 2 + t


def salvar_grafico(nome_arquivo: str) -> None:
    caminho = os.path.join("graficos", nome_arquivo)

    plt.tight_layout()
    plt.savefig(caminho, dpi=300, bbox_inches="tight")
    plt.close()

# 1. Apresente a solução para a EDP hiperbólica não homogênea;

x = np.linspace(-10, 20, 1000)
tempos = [0, 1, 2, 3, 4]

plt.figure(figsize=(10, 6))

for t in tempos:
    plt.plot(x, u(x, t), label=f"t = {t}")

plt.xlabel("Posição x")
plt.ylabel("u(x,t)")
plt.title("Solução da EDP para diferentes valores de tempo")
plt.grid(True)
plt.legend()

salvar_grafico("01_solucao_edp.png")

t_valores = np.linspace(0, 5, 300)

# 2. Represente graficamente as ondas formadas em diferentes valores de t.

x_superficie = np.linspace(-10, 20, 300)
t_superficie = np.linspace(0, 5, 200)

X, T = np.meshgrid(x_superficie, t_superficie)

U = u(X, T)

fig = plt.figure(figsize=(11, 7))
ax = fig.add_subplot(111, projection="3d")

superficie = ax.plot_surface(X, T, U, cmap="viridis")

ax.set_xlabel("Posição x")
ax.set_ylabel("Tempo t")
ax.set_zlabel("u(x,t)")
ax.set_title(
    "Superfície da solução "
    "u(x,t) = (x - 3t)² + t"
)

fig.colorbar(superficie, ax=ax, shrink=0.6, label="u(x,t)")

salvar_grafico("02_representacao_grafica.png")