from math import factorial
import numpy as np
import matplotlib.pyplot as plt
from data import x, y, xMin, yMin, xMax, yMax, h

def Z(x):
    return ((x-xMin[0])/h)

def Z_1(x):
    return ((x-xMin[0]-1)/h)

def Z_2(x):
    return ((x-xMin[0]-2)/h)

def firstOrderDiff():
    FOD = []

    for i in range(len(yMin)):
        if(i==0):
            continue
        else:
            aux = yMin[i] - yMin[i-1]
            FOD.append(aux)
    
    return FOD

def secondOrderDiff(FOD):
    SOD = []

    for i in range(len(FOD)):
        if(i==0):
            continue
        else:
            aux = FOD[i] - FOD[i-1]
            SOD.append(aux)
    
    return SOD

def thirdOrderDiff(SOD):
    TOD = []

    for i in range(len(SOD)):
        if(i==0):
            continue
        else:
            aux = SOD[i] - SOD[i-1]
            TOD.append(aux)
    
    return TOD

def polynomial(x, fod, sod, tod):
    return ( (yMin[0]) + ((Z(x))*(fod[0])/factorial(1)) + ((Z(x))*(Z_1(x))*(sod[0])/factorial(2)) + ((Z(x))*(Z_1(x))*(Z_2(x))*(tod[0])/factorial(3))) 

def createMinFunction(FOD, SOD, TOD):
    
    func = []

    xValues = np.linspace(xMin[0], xMin[3], 100)
    for i in range(len(xValues)):
        func.append(polynomial(xValues[i], FOD, SOD, TOD))

    for i in range(len(func)):
        if(i==0):
            minDemand = func[i]
        else:
            if(func[i]<minDemand):
                minDemand = func[i]
                minTime = xValues[i]
            else:
                continue

    return minTime, minDemand


def plotMinGraphics(minTime, minDemand, fod, sod, tod):
    plt.grid()
    plt.title(f'Estimativa da demanda no período de mínima.\nMenor valor encontrado para a demanda: {minDemand:.2f}, na hora {minTime:.2f}')
    plt.scatter(minTime, minDemand, color='yellow')
    plt.xlabel('X(Tempo em horas)')
    plt.ylabel('Y(Demanda)')
    plt.scatter(xMin, yMin, color='blue')
    plt.plot(
        np.linspace(xMin[0], xMin[3], 100),
        polynomial(np.linspace(xMin[0], xMin[3], 100), fod, sod, tod)
    )
    plt.show()
