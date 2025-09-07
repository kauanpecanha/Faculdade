import numpy as np

def solve_rk4(f, y0, t, h):
    """
    Resolve um sistema de EDOs usando o método RK4.
    f: função que retorna derivadas [dG, dF]
    y0: vetor de condições iniciais [G_init, F_init]
    t: vetor de tempo
    h: passo
    """
    n = len(t)
    y = np.zeros((n, len(y0)))
    y[0] = y0

    for i in range(1, n):
        k1 = f(y[i-1])
        k2 = f(y[i-1] + h/2 * k1)
        k3 = f(y[i-1] + h/2 * k2)
        k4 = f(y[i-1] + h * k3)
        y[i] = y[i-1] + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
    return y