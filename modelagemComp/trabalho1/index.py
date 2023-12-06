import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

xArr = pd.read_csv("dados.csv")["X"] # definição da matriz X
yArr = pd.read_csv("dados.csv")["Y"] # definição da matriz Y

sum_xi0 = sum([xArr[i] ** 0 for i in range(len(xArr))])
sum_xi1 = sum([xArr[i] ** 1 for i in range(len(xArr))])
sum_xi2 = sum([xArr[i] ** 2 for i in range(len(xArr))])
sum_xi3 = sum([xArr[i] ** 3 for i in range(len(xArr))])
sum_xi4 = sum([xArr[i] ** 4 for i in range(len(xArr))])
sum_xi5 = sum([xArr[i] ** 5 for i in range(len(xArr))])
sum_xi6 = sum([xArr[i] ** 6 for i in range(len(xArr))])
sum_xi7 = sum([xArr[i] ** 7 for i in range(len(xArr))])
sum_xi8 = sum([xArr[i] ** 8 for i in range(len(xArr))])
sum_xi9 = sum([xArr[i] ** 9 for i in range(len(xArr))])
sum_xi10 = sum([xArr[i] ** 10 for i in range(len(xArr))])

n = len(xArr)

sum_yi = sum([yArr[i] for i in range(len(yArr))])
sum_yixi = sum([yArr[i] * xArr[i] for i in range(len(yArr))])
sum_yixi2 = sum([yArr[i] * (xArr[i] ** 2) for i in range(len(yArr))])
sum_yixi3 = sum([yArr[i] * (xArr[i] ** 3) for i in range(len(yArr))])
sum_yixi4 = sum([yArr[i] * (xArr[i] ** 4) for i in range(len(yArr))])
sum_yixi5 = sum([yArr[i] * (xArr[i] ** 5) for i in range(len(yArr))])

y = np.array([
    [sum_yi],
    [sum_yixi],
    [sum_yixi2],
    [sum_yixi3],
    [sum_yixi4],
    [sum_yixi5],
])

x = np.array([
    [n, sum_xi1, sum_xi2, sum_xi3, sum_xi4, sum_xi5],
    [sum_xi1, sum_xi2, sum_xi3, sum_xi4, sum_xi5, sum_xi6],
    [sum_xi2, sum_xi3, sum_xi4, sum_xi5, sum_xi6, sum_xi7],
    [sum_xi3, sum_xi4, sum_xi5, sum_xi6, sum_xi7, sum_xi8],
    [sum_xi4, sum_xi5, sum_xi6, sum_xi7, sum_xi8, sum_xi9],
    [sum_xi5, sum_xi6, sum_xi7, sum_xi8, sum_xi9, sum_xi10],
])

x_transpose = np.linalg.inv(x)

beta = x_transpose @ x

beta = np.linalg.inv(beta)

beta = beta @ x_transpose

beta = beta @ y

print(beta)

plt.scatter(xArr, yArr)

def function(x, beta): # função de previsão utilizando dos coeficientes encontrados
    # b0 * x ** 0 + b1 * x ** 1 + b2 * x**2 + b3 * x**3 + b4 * x**4
    return beta[0] * (x ** 0) + beta[1] * (x) + beta[2] * (x**2) + beta[3] * (x**3) + beta[4] * (x**4) + beta[5] * (x**5)

yf = [] # vetor para armazenar os valores de y de acordo com a função resultante
for i in range(len(xArr)):
    yf.append(function(xArr[i], beta)) # armazenamento dos valores

plt.plot(xArr, yf)
plt.show()

# 1 - Se houver, em que momento o preço das ações deixa de ter um comportamento decrescente?
interval = np.linspace(xArr[len(xArr)-1], 5, 1000)
y_interval = []
for i in range(len(interval)):
    y_interval.append(function(interval[i], beta))

plt.plot(interval, y_interval, color="purple")
plt.scatter(xArr[len(xArr)-1], yArr[len(yArr)-1], color="red") # plotagem do momento de entrada
plt.scatter(4+(5/12), function(4+(5/12), beta), color="green") # plotagem do momento de saída 1
plt.scatter(4+(8/12), function(4+(8/12), beta), color="green") # plotagem do momento de saída 2
plt.scatter(4+(12/12), function(4+(12/12), beta), color="green") # plotagem do momento de saída 3
plt.show()

# Gráfico todo

plt.scatter(xArr, yArr)
plt.plot(xArr, yf)
plt.plot(interval, y_interval, color="purple")
plt.scatter(xArr[len(xArr)-1], yArr[len(yArr)-1], color="red") # plotagem do momento de entrada
plt.scatter(4+(5/12), function(4+(5/12), beta), color="green") # plotagem do momento de saída 1
plt.scatter(4+(8/12), function(4+(8/12), beta), color="green") # plotagem do momento de saída 2
plt.scatter(4+(12/12), function(4+(12/12), beta), color="green") # plotagem do momento de saída 3

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
