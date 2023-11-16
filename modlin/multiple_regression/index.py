import numpy as np
from math import sqrt

x = np.array([
    [1, 31, 4],
    [1, 16, 5],
    [1, 29, 3],
    [1, 19, 0],
    [1, 27, 2],
])

y = np.array([
    [12],
    [18],
    [3],
    [3],
    [11],
])

x_transpose = np.transpose(x)

prodx = np.dot(x_transpose, x)

prodx_inv = np.linalg.inv(prodx)

prod = np.dot(prodx_inv, x_transpose)

beta = np.dot(prod, y)

print(f"Equação do MRLM: {beta[0][0]:.2f} + {beta[1][0]:.2f} * x1 + {beta[2][0]:.2f} * x2")

# # montagem da tabela anova
# n = 5
# p = 2
# coef = 5.65
# # coef = float(input("Entre com o coeficiente: "))

# y_med = np.mean(y)

# y_transpose = np.transpose(y)

# sqt = ( np.dot(y_transpose, y) ) - ( n * (y_med**2) )

# beta_transpose = (np.transpose(beta))

# sqreg = ( np.dot(np.dot(beta_transpose, x_transpose), y)) - ( n * (y_med**2) )

# sqe = sqt - sqreg

# # print(sqt[0][0])
# # print(sqreg[0][0])
# # print(sqe[0][0])

# sqreg = float(sqreg[0][0])
# sqt = float(sqt[0][0])
# sqe = float(sqe[0][0])

# gl = np.array([p, n-p-1, n-1])
# sq = np.array([sqreg, sqe, sqt])
# qm = np.array([(sqreg/p), (sqe/n-p-1), 0])
# f0 = np.array([((sqreg/p)/(sqe/n-p-1)), 0, 0])


# # for i in range(len(gl)):
#     # print(f"{gl[i]:.2f} \t {sq[i]:.2f} \t {qm[i]:.2f} \t {f0[i]:.2f}")

# if f0[0] > coef:
#     print(f"Hipótese H0 rejeitada(modelo de regressão linear múltipla)")
# else:
#     print(f"Hipótese H1 rejeitada(modelo simples)")


# # Estatística de Teste de Hipótese

# tau_square = (np.dot((np.transpose((y - (np.dot(x, beta))))), (y - (np.dot(x, beta))))/n - p - 1)
# tau_square = tau_square[0][0]

# comparisson_constant = 4.21

# # print(tau_square)
# # print(prodx_inv)


# for k in range(0, len(beta)):
#     print(k)
#     t_bk = beta[k]/sqrt(tau_square * prodx_inv[k][k])
    
#     if t_bk**2 >= comparisson_constant:
#         print(f"Para {beta[k]}, a hipótese nula é rejeitada.\nValor de t_bk**2 = {t_bk**2}\n")
#     else:
#         print(f"Para {beta[k]}, a hipótese não-nula é rejeitada.\nValor de t_bk**2 = {t_bk**2}\n")