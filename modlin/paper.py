from math import *
import numpy as np

from mlrm import beta, x, y, n, p, prodx_inv

tau_square = (np.dot((np.transpose((y - (np.dot(x, beta))))), (y - (np.dot(x, beta))))/n - p - 1)
tau_square = tau_square[0][0]

comparisson_constant = 4.21

# print(tau_square)
# print(prodx_inv)


for k in range(0, len(beta)):
    print(k)
    t_bk = beta[k]/sqrt(tau_square * prodx_inv[k][k])
    
    if t_bk >= comparisson_constant:
        print(f"Para {beta[k]}, a hipótese nula é rejeitada.\nValor de t_bk = {t_bk}\n")
    else:
        print(f"Para {beta[k]}, a hipótese não-nula é rejeitada.\nValor de t_bk = {t_bk}\n")