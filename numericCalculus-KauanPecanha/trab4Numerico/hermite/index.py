import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, expand, diff

# Matriz de entrada contendo os valores de tempo, distância e velocidade
# matriz = np.array([[0.0, 3.0, 5.0],
#                    [0.0, 261.0, 339.0],
#                    [75.0, 77.0, 62.0]])

matriz = np.array([[0.0, 3.0, 5.0, 8.0, 13.0, 17.0],
                   [0.0, 261.0, 339.0, 645.0, 993.0, 999.0],
                   [75.0, 77.0, 62.0, 78.0, 72.0, 77.0]])

x = matriz[0]  # Valores de tempo
y = matriz[1]  # Valores de distância
dy = matriz[2]  # Valores de velocidade

def hermite(x, fx, fx_):
    divided_diff = []
    divided_diff.append(fx_)  # Primeiras diferenças divididas (primeira ordem)

    for i in range(1, len(x)):
        differences = []
        for j in range(len(divided_diff[i - 1]) - 1):
            numerator = divided_diff[i - 1][j + 1] - divided_diff[i - 1][j]
            denominator = x[i + j] - x[j]
            differences.append(numerator / denominator)
        divided_diff.append(differences)

    X = symbols('x')
    polynomial = fx[0]
    term = 1
    for i in range(len(divided_diff)):
        term *= (X - x[i])
        polynomial += divided_diff[i][0] * term

    polynomial = expand(polynomial)
    print("Polynomial:", polynomial)

    derivative = diff(polynomial, X)
    print("Derivative:", derivative)

    coefficients = polynomial.as_coefficients_dict()  # Coeficientes do polinômio
    return polynomial, derivative, coefficients

def mph_to_mps(mph):
    return mph * 0.44704  # Função que irá converter milhas/h para metros/segundo

# Chamada da função => Convertendo velocidades de mph para m/s
dy_mps = mph_to_mps(dy)

# Verificando se o limite de velocidade foi excedido
exceeded_limit = False
exceeded_time = None

# Se atingir 55 milhas, irá retornar verdadeiro
for i in range(len(x)):
    polynomial, derivative, coefficients = hermite(x, y, dy_mps)
    velocity = np.polyval(list(coefficients.values())[::-1], x[i])
    if velocity > mph_to_mps(55):
        exceeded_limit = True
        exceeded_time = x[i]
        break

if exceeded_limit:
    print("O limite de velocidade de 55 milhas/h foi excedido pela primeira vez em", exceeded_time, "segundos.")
else:
    print("O limite de velocidade de 55 milhas/h não foi excedido.")

# Plotar o gráfico
X = symbols('x')
X_value = 5.4
y_ponto = derivative.subs('x', X_value)

x_vals = np.linspace(0, 17)
y_vals = [derivative.subs('x', val) for val in x_vals]

maxVel = max(y_vals)
limit = mph_to_mps(55)

plt.plot(x_vals, y_vals, label='Equação: y = ' + str(derivative))
plt.scatter(X_value, y_ponto, color='red', label='Ponto')

plt.xlabel('Tempo')
plt.ylabel('Velocidade')
plt.title('Gráfico da Equação')
plt.xlim(1, 17)
plt.ylim(-8, 300)
plt.legend()
plt.show()

print(f'O valor máximo da velocidade é de: {maxVel} mps.')
print(f'O valor de 55 mph corresponde a {limit} mps')