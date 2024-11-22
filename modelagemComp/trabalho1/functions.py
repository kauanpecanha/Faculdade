# importação das bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# função de cálculo de coeficientes beta
def solveMatrix(x_matrix, y_matrix):

    # observação: importante saber que @ efetua uma operação entre matrizes, em
    # python

    # determinação da transposta
    x_transpose = np.linalg.inv(x_matrix)

    # produto da transposta pela original
    beta = x_transpose @ x_matrix

    # cálculo da inversa
    beta = np.linalg.inv(beta)

    # produto pela transposta
    beta = beta @ x_transpose

    # produto pela matriz y
    beta = beta @ y_matrix

    # retorno dos coeficientes beta    
    return beta

# função de previsão utilizando dos coeficientes encontrados
def function(x_value, beta):
    # b0 * x ** 0 + b1 * x ** 1 + b2 * x**2 + b3 * x**3 + b4 * x**4
    return (
        beta[0] * (x_value ** 0) +
        beta[1] * (x_value ** 1) +
        beta[2] * (x_value ** 2) +
        beta[3] * (x_value ** 3) +
        beta[4] * (x_value ** 4) +
        beta[5] * (x_value ** 5)
    )

def setInterval(x_data, beta):
    
    # criação de um array com 1000 pontos entre o último ponto dado por x e 5
    x_interval = np.linspace(x_data[len(x_data)-1], 5, 1000)
    y_interval = []
    
    # cálculo dos valores de y correspondentes à interpolação, para tais valores
    for i in range(len(x_interval)):
        y_interval.append(function(x_interval[i], beta))
    
    # retorno de tais valores
    return x_interval, y_interval

# função de plotagem dos gráficos necessários
def plotGraphic(x_data, y_data, beta, y_function, x_interval, y_interval, key, grid = True):

    # explicação do funcionamento: esta função tem o intuito de centralizar nela
    # toda a responsabilidade de plotagem de gráficos.
    # A disntição se dá através do atributo key, o qual especifica qual o gráfico
    # desejado.

    if key == 1:
        # Caso 1, será plotado o gráfico com todos os dados fornecidos pelo csv
        if grid == True:
            plt.grid()
        
        plt.scatter(x_data, y_data, label="Dados")
        plt.title("Gráfico valor da ação x Tempo")
        plt.xlabel("Tempo (em anos)")
        plt.ylabel("Valor da ação (em reais)")
        plt.legend()
        plt.show()

    elif key == 2:
        # Caso 2, será plotado o gráfico com a regressão polinomial obtida após as
        # operações matemáticas necessárias serem executadas.
        if grid == True:
            plt.grid()
        
        plt.scatter(x_data, y_data, label="Dados")
        plt.title("Regressão polinomial")
        plt.xlabel("Tempo (em anos)")
        plt.ylabel("Valor da ação (em reais)")
        plt.plot(x_data, y_function, label="Regressão polinomial")
        plt.legend()
        plt.show()

    elif key == 3:
        # Caso 3, será plotado o valor da ação de acordo com a previsão da
        # regressão polinomial.
        if grid == True:
            plt.grid()
        
        plt.title("Regressão polinomial")
        plt.xlabel("Tempo (em anos)")
        plt.ylabel("Valor da ação (em reais)")
        plt.plot(x_data, y_function, label="Regressão polinomial")
        plt.legend()
        plt.show()

    elif key == 4:
        # Caso 4, será plotado o valor da ação no primeiro tempo pedido no
        # enunciado da questão.
        if grid == True:
            plt.grid()
        
        plt.title(f"Previsão quando t = [4, {( (4) + (5/12) ):.2f}]")
        plt.xlabel("Tempo (em anos)")
        plt.ylabel("Valor da ação (em reais)")
        plt.plot(x_interval, y_interval, color="purple", label="Previsão t=[4, 5]")
        
        # plotagem do momento de entrada
        plt.scatter(x_data[len(x_data)-1], y_data[len(y_data)-1], color="red", label="Entrada")
        # plotagem do momento de saída 1
        plt.scatter(4+(5/12), function(4+(5/12), beta), color="green", label="Saída 1")
        
        plt.legend()
        plt.show()

    elif key == 5:
        # Caso 5, será plotado o valor da ação no segundo tempo pedido no
        # enunciado da questão.
        if grid == True:
            plt.grid()
        
        plt.title(f"Previsão quando t = [4, {( (4) + (8/12) ):.2f}]")
        plt.xlabel("Tempo (em anos)")
        plt.ylabel("Valor da ação (em reais)")
        plt.plot(x_interval, y_interval, color="purple", label="Previsão t=[4, 5]")

        # plotagem do momento de entrada
        plt.scatter(x_data[len(x_data)-1], y_data[len(y_data)-1], color="red", label="Entrada")
        # plotagem do momento de saída 2
        plt.scatter(4+(8/12), function(4+(8/12), beta), color="brown", label="Saída 2")

        plt.legend()
        plt.show()

    elif key == 6:
        # Caso 6, será plotado o valor da ação no terceiro tempo pedido no
        # enunciado da questão.
        if grid == True:
            plt.grid()

        plt.title("Previsão quando t = [4, 5]")
        plt.xlabel("Tempo (em anos)")
        plt.ylabel("Valor da ação (em reais)")
        plt.plot(x_interval, y_interval, color="purple", label="Previsão t=[4, 5]")

        # plotagem do momento de entrada
        plt.scatter(x_data[len(x_data)-1], y_data[len(y_data)-1], color="red", label="Entrada")
        # plotagem do momento de saída 3
        plt.scatter(4+(12/12), function(4+(12/12), beta), color="aqua", label="Saída 3")

        plt.legend()
        plt.show()

    elif key == 7:
        # Caso 7, serão plotados os três valores da ação previstos, no mesmo
        # gráfico
        if grid == True:
            plt.grid()

        plt.title("Gráfico Total")
        plt.xlabel("Tempo (em anos)")
        plt.ylabel("Valor da Ação (em reais)")
        plt.scatter(x_data, y_data, label="Dados")
        plt.plot(x_data, y_function, label="Regressão polinomial")
        plt.plot(x_interval, y_interval, color="purple", label="Previsão polinomial")
        
        # plotagem do momento de entrada
        plt.scatter(x_data[len(x_data)-1], y_data[len(y_data)-1], color="red", label="Entrada")

        # plotagem do momento de saída 1
        plt.scatter(4+(5/12), function(4+(5/12), beta), color="green", label="Saída 1")
        # plotagem do momento de saída 2
        plt.scatter(4+(8/12), function(4+(8/12), beta), color="brown", label="Saída 2")
        # plotagem do momento de saída 3
        plt.scatter(4+(12/12), function(4+(12/12), beta), color="aqua", label="Saída 3")

        plt.legend()
        plt.show()

    elif key == 8:
        # Caso 8, será plotado o gráfico sem os pontos, ou seja, apenas com o
        # comportamento das funções
        if grid == True:
            plt.grid()

        plt.title("Gráfico Total")
        plt.xlabel("Tempo (em anos)")
        plt.ylabel("Valor da Ação (em reais)")
        
        plt.plot(x_data, y_function, label="Regressão polinomial")
        plt.plot(x_interval, y_interval, color="purple", label="Previsão polinomial")
        plt.legend()
        plt.show()

# função de definição do modelo linear
def linearModel(x_data, beta):
    yf = []

    for i in range(len(x_data)):
        yf.append(function(x_data[i], beta))

    return yf