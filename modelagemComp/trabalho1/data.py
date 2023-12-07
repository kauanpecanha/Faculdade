import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from functions import solveMatrix, setInterval, function, linearModel

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

beta = solveMatrix(x, y)

interval, y_interval = setInterval(xArr, beta)

cost = 1000 * yArr[len(yArr)-1] # determinação do valor gasto na compra de 1000 ações quando t = 4 anos

sellingValue1 = 1000 * function(x_value = 4 + (5/12), beta = beta) # determinação do valor gasto na venda de 1000 ações quando t = 4 anos e 5 meses
sellingValue2 = 1000 * function(x_value = 4 + (8/12), beta = beta) # determinação do valor gasto na venda de 1000 ações quando t = 4 anos e 8 meses
sellingValue3 = 1000 * function(x_value = 4 + (12/12), beta = beta) # determinação do valor gasto na venda de 1000 ações quando t = 4 anos e 12 meses ou 5 anos

yf = linearModel(xArr, beta)