import numpy as np

def compute_svd_via_eigendecomposition(A):
    """
    Calcula a decomposição SVD de A utilizando autovetores e autovalores.
    :param A: Matriz de coeficientes (numpy array de dimensão mxn)
    :return: Matrizes U, S, Vt
    """
    # Calcular autovalores e autovetores de AAt e AtA
    AAt = np.dot(A, A.T)
    AtA = np.dot(A.T, A)
    eigvals_AAt, U = np.linalg.eigh(AAt)
    eigvals_AtA, V = np.linalg.eigh(AtA)
    # Ordenar os autovalores em ordem decrescente e ajustar os autovetores
    idx_U = np.argsort(eigvals_AAt)[::-1]
    idx_V = np.argsort(eigvals_AtA)[::-1]
    U = U[:, idx_U]
    V = V[:, idx_V]
    # Valores singulares são as raízes quadradas dos autovalores de AtA
    S = np.sqrt(eigvals_AtA[idx_V])
    # Criar matriz diagonal S
    S_matrix = np.diag(S)
    return U, S_matrix, V.T

def solve_linear_svd(A, b):
    """
    Resolve o sistema linear Ax = b usando SVD calculado por autovalores/autovetores.
    :param A: Matriz de coeficientes (numpy array de dimensão mxn)
    :param b: Vetor de termos independentes (numpy array de dimensão m)
    :return: Vetor solução x
    """
    U, S, Vt = compute_svd_via_eigendecomposition(A)
    # Resolver para y no sistema Uy = b
    y = np.dot(U.T, b) / np.diag(S)
    # Resolver para x no sistema Vx = y
    x = np.dot(Vt.T, y)
    return x

# Exemplo de uso
A = np.array([[2, 2], [-1, 1]])
b = np.array([0, 0])

x = solve_linear_svd(A, b)
print("Solução x:", x)
