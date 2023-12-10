import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def solveMatrix(x_matrix, y_matrix):
    
    x_transpose = np.linalg.inv(x_matrix)

    beta = x_transpose @ x_matrix

    beta = np.linalg.inv(beta)

    beta = beta @ x_transpose

    beta = beta @ y_matrix
    
    return beta

def function(x_value, beta): # função de previsão utilizando dos coeficientes encontrados
    # b0 * x ** 0 + b1 * x ** 1 + b2 * x**2 + b3 * x**3 + b4 * x**4
    return beta[0] * (x_value ** 0) + beta[1] * (x_value) + beta[2] * (x_value**2) + beta[3] * (x_value**3) + beta[4] * (x_value**4) + beta[5] * (x_value**5)

def setInterval(x_data, beta):
    
    x_interval = np.linspace(x_data[len(x_data)-1], 5, 1000)
    y_interval = []
    
    for i in range(len(x_interval)):
        y_interval.append(function(x_interval[i], beta))
    
    return x_interval, y_interval

def plotGraphic(x_data, y_data, beta, y_function, x_interval, y_interval, key, grid = True):
    
    if key == 1:
        if grid == True:
            plt.grid()
        plt.scatter(x_data, y_data, label="Dados")
        plt.title("Gráfico valor da ação x Tempo")
        plt.xlabel("Tempo (em anos)")
        plt.ylabel("Valor da ação (em reais)")
        plt.legend()
        plt.show()
    elif key == 2:
        plt.scatter(x_data, y_data, label="Dados")
        if grid == True:
            plt.grid()
        plt.title("Regressão polinomial")
        plt.xlabel("Tempo (em anos)")
        plt.ylabel("Valor da ação (em reais)")
        plt.plot(x_data, y_function, label="Regressão polinomial")
        plt.legend()
        plt.show()
    elif key == 3:
        # plt.scatter(x_data, y_data, label="Dados")
        if grid == True:
            plt.grid()
        plt.title("Regressão polinomial")
        plt.xlabel("Tempo (em anos)")
        plt.ylabel("Valor da ação (em reais)")
        plt.plot(x_data, y_function, label="Regressão polinomial")
        plt.legend()
        plt.show()
    elif key == 4:
        plt.title(f"Previsão quando t = [4, {( (4) + (5/12) ):.2f}]")
        plt.xlabel("Tempo (em anos)")
        plt.ylabel("Valor da ação (em reais)")
        if grid == True:
            plt.grid()
        plt.plot(x_interval, y_interval, color="purple", label="Previsão t=[4, 5]")
        plt.scatter(x_data[len(x_data)-1], y_data[len(y_data)-1], color="red", label="Entrada") # plotagem do momento de entrada
        plt.scatter(4+(5/12), function(4+(5/12), beta), color="green", label="Saída 1") # plotagem do momento de saída 1
        # plt.scatter(4+(8/12), function(4+(8/12), beta), color="brown", label="Saída 2") # plotagem do momento de saída 2
        # plt.scatter(4+(12/12), function(4+(12/12), beta), color="aqua", label="Saída 3") # plotagem do momento de saída 3
        plt.legend()
        plt.show()
    elif key == 5:
        plt.title(f"Previsão quando t = [4, {( (4) + (8/12) ):.2f}]")
        plt.xlabel("Tempo (em anos)")
        plt.ylabel("Valor da ação (em reais)")
        if grid == True:
            plt.grid()
        plt.plot(x_interval, y_interval, color="purple", label="Previsão t=[4, 5]")
        plt.scatter(x_data[len(x_data)-1], y_data[len(y_data)-1], color="red", label="Entrada") # plotagem do momento de entrada
        # plt.scatter(4+(5/12), function(4+(5/12), beta), color="green", label="Saída 1") # plotagem do momento de saída 1
        plt.scatter(4+(8/12), function(4+(8/12), beta), color="brown", label="Saída 2") # plotagem do momento de saída 2
        # plt.scatter(4+(12/12), function(4+(12/12), beta), color="aqua", label="Saída 3") # plotagem do momento de saída 3
        plt.legend()
        plt.show()
    elif key == 6:
        plt.title("Previsão quando t = [4, 5]")
        plt.xlabel("Tempo (em anos)")
        plt.ylabel("Valor da ação (em reais)")
        if grid == True:
            plt.grid()
        plt.plot(x_interval, y_interval, color="purple", label="Previsão t=[4, 5]")
        plt.scatter(x_data[len(x_data)-1], y_data[len(y_data)-1], color="red", label="Entrada") # plotagem do momento de entrada
        # plt.scatter(4+(5/12), function(4+(5/12), beta), color="green", label="Saída 1") # plotagem do momento de saída 1
        # plt.scatter(4+(8/12), function(4+(8/12), beta), color="brown", label="Saída 2") # plotagem do momento de saída 2
        plt.scatter(4+(12/12), function(4+(12/12), beta), color="aqua", label="Saída 3") # plotagem do momento de saída 3
        plt.legend()
        plt.show()
    elif key == 7:
        if grid == True:
            plt.grid()
        plt.title("Gráfico Total")
        plt.xlabel("Tempo (em anos)")
        plt.ylabel("Valor da Ação (em reais)")
        plt.scatter(x_data, y_data, label="Dados")
        plt.plot(x_data, y_function, label="Regressão polinomial")
        plt.plot(x_interval, y_interval, color="purple", label="Previsão polinomial")
        plt.scatter(x_data[len(x_data)-1], y_data[len(y_data)-1], color="red", label="Entrada") # plotagem do momento de entrada
        plt.scatter(4+(5/12), function(4+(5/12), beta), color="green", label="Saída 1") # plotagem do momento de saída 1
        plt.scatter(4+(8/12), function(4+(8/12), beta), color="brown", label="Saída 2") # plotagem do momento de saída 2
        plt.scatter(4+(12/12), function(4+(12/12), beta), color="aqua", label="Saída 3") # plotagem do momento de saída 3
        plt.legend()
        plt.show()
    elif key == 8:
        if grid == True:
            plt.grid()
        plt.title("Gráfico Total")
        plt.xlabel("Tempo (em anos)")
        plt.ylabel("Valor da Ação (em reais)")
        # plt.scatter(x_data, y_data, label="Dados")
        plt.plot(x_data, y_function, label="Regressão polinomial")
        plt.plot(x_interval, y_interval, color="purple", label="Previsão polinomial")
        # plt.scatter(x_data[len(x_data)-1], y_data[len(y_data)-1], color="red", label="Entrada") # plotagem do momento de entrada
        # plt.scatter(4+(5/12), function(4+(5/12), beta), color="green", label="Saída 1") # plotagem do momento de saída 1
        # plt.scatter(4+(8/12), function(4+(8/12), beta), color="brown", label="Saída 2") # plotagem do momento de saída 2
        # plt.scatter(4+(12/12), function(4+(12/12), beta), color="aqua", label="Saída 3") # plotagem do momento de saída 3
        plt.legend()
        plt.show()

def linearModel(x_data, beta):
    yf = []
    
    for i in range(len(x_data)):
        yf.append(function(x_data[i], beta))
    
    return yf