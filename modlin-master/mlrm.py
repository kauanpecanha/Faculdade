import numpy as np

x = np.array([
    [1, 31, 4],
    [1, 16, 5],
    [1, 29, 3],
    [1, 19, 0],
    [1, 21, 2],
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

# print(prodx)

prodx_inv = np.linalg.inv(prodx)

# print(prodx_inv)

xty = np.dot(x_transpose, y)

# print(xty)

beta = np.dot(prodx_inv, xty)

# print(beta)

print(f"Equação do MRLM: {beta[0][0]:.2f} + {beta[1][0]:.2f} * x1 + {beta[2][0]:.2f} * x2")