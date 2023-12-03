import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
from scipy import linalg

xArr = pd.read_csv("dados.csv")["X"] # definição da matriz X
yArr = pd.read_csv("dados.csv")["Y"] # definição da matriz Y

grau = 5 # grau pedido

# Criação da matriz de 101x6, composta pelos coeficientes de x que deram origem aos valores de yArr
X = np.zeros((len(yArr), grau + 1)) # criação da matriz de zeros das dimensões especificadas(nesse caso, 101x6) - 6, pois o primeiro índice é 1, ou seja, grau 0, e de 0 a 5, são seis números

for i in range(len(yArr)): # para cada linha
    
    for j in range(grau + 1): # para cada coluna
        
        X[i, j] = xArr[i] ** j # o elemento da matriz de vandermonde é o elemento em questão da matriz x, elevado ao grau em questão
        
beta = np.linalg.lstsq(X, yArr)[0] # resolução linear dessa matriz para determinação dos coeficientes

def function(x, beta): # função de previsão utilizando dos coeficientes encontrados
    # b0 + b1 * x + b2 * x**2 + b3 * x**3 + b4 * x**4 + b5 * x**5
    return beta[0] + beta[1] * (x) + beta[2] * (x**2) + beta[3] * (x**3) + beta[4] * (x**4) + beta[5] * (x**5)

yf = [] # vetor para armazenar os valores de y de acordo com a função resultante
for i in range(len(xArr)):
    yf.append(function(xArr[i], beta)) # armazenamento dos valores

# --------------------------------Plotagem dos Gráficos----------------------------------------------------------------------------------------
plt.grid()
plt.scatter(xArr, yArr)
plt.plot(xArr, yf)

# 1 - Se houver, em que momento o preço das ações deixa de ter um comportamento decrescente?
interval = np.linspace(xArr[len(xArr)-1], 5, 1000)
y_interval = []
for i in range(len(interval)):
    y_interval.append(function(interval[i], beta))

plt.plot(interval, y_interval, color="orange")

# ------------------------------------------------------------------------------------------------------------------------


# Resposta: Quando o preço das ações é de, aproximadamente, R$4,50

# Qual seria o lucro (ou prejuízo) do investidor, caso as ações fossem vendidas considerando-se os cenários:
    # a) Cinco meses após a compra;
    # a) Oito meses após a compra;
    # a) Doze meses após a compra;
    
    
# ------------------ Desenvolvimento ----------------------------
# 1000 ações compradas quando t = 4 anos

cost = 1000 * yArr[len(yArr)-1] # determinação do valor gasto na compra de 1000 ações quando t = 4 anos

sellingValue1 = 1000 * function(x = 4 + (5/12), beta = beta) # determinação do valor gasto na venda de 1000 ações quando t = 4 anos e 5 meses
sellingValue2 = 1000 * function(x = 4 + (8/12), beta = beta) # determinação do valor gasto na venda de 1000 ações quando t = 4 anos e 8 meses
sellingValue3 = 1000 * function(x = 4 + (12/12), beta = beta) # determinação do valor gasto na venda de 1000 ações quando t = 4 anos e 12 meses ou 5 anos

plt.scatter(xArr[len(xArr)-1], yArr[len(yArr)-1], color="red") # plotagem do momento de entrada
plt.scatter(4+(5/12), function(4+(5/12), beta), color="green") # plotagem do momento de saída 1
plt.scatter(4+(8/12), function(4+(8/12), beta), color="green") # plotagem do momento de saída 2
plt.scatter(4+(12/12), function(4+(12/12), beta), color="green") # plotagem do momento de saída 3

# impressão das informações de venda
print(f"\n\nVENDA\n\nO valor que ele conseguiria através da venda das ações estão listados abaixo:\n\ta) Cinco meses após a compra: R${sellingValue1:.2f}\n\tb) Oito meses após a compra: R${sellingValue2:.2f}\n\tc) Doze meses após a compra: R${sellingValue3:.2f}")

# impressão das informações de lucro
print(f"\n\nLUCRO\n\nOs valores de lucro são listados abaixo:\n\ta)Cinco meses após a compra: R${(sellingValue1 - cost):.2f}\n\tb)Oito meses após a compra: R${(sellingValue2 - cost):.2f}\n\tc)Doze meses após a compra: R${(sellingValue3 - cost):.2f}")

# impressão final do gráfico
plt.show()

# Respostas: 
    # a) Prejuízo de R$595,00 reais
    # a) Lucro de R$6.526,52 reais
    # a) Lucro de R$33.136,00 reais