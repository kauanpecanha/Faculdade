import matplotlib.pyplot as plt
import numpy as np
from math import factorial
from data import x, y, xMax, yMax, h

# estimativa da demanda mínima

def Z(x):
    return ((x-xMax[0])/h)

def Z_1(x):
    return ((x-xMax[0]-1)/h)

def Z_2(x):
    return ((x-xMax[0]-2)/h)

def firstOrderDiff():
    FOD = []

    for i in range(len(yMax)):
        if(i==0):
            continue
        else:
            aux = yMax[i] - yMax[i-1]
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
    return ( (yMax[0]) + ((Z(x))*(fod[0])/factorial(1)) + ((Z(x))*(Z_1(x))*(sod[0])/factorial(2)) + ((Z(x))*(Z_1(x))*(Z_2(x))*(tod[0])/factorial(3))) 

def createMaxFunction(FOD, SOD, TOD):
    
    func = []

    xValues = np.linspace(xMax[0], xMax[3], 100)
    for i in range(len(xValues)):
        func.append(polynomial(xValues[i], FOD, SOD, TOD))

    for i in range(len(func)):
        if(i==0):
            maxDemand = func[i]
        else:
            if(func[i]>maxDemand):
                maxDemand = func[i]
                maxTime = xValues[i]
            else:
                continue
    return maxTime, maxDemand


def plotMaxGraphics(maxTime, maxDemand, fod, sod, tod):
    plt.grid()
    plt.title(f'Estimativa da demanda no período de máxima.\nMaior valor encontrado para a demanda: {maxDemand:.2f}, na hora {maxTime:.2f}')
    plt.scatter(maxTime, maxDemand, color='yellow')
    plt.xlabel('X(Tempo em horas)')
    plt.ylabel('Y(Demanda)')
    plt.scatter(xMax, yMax, color='blue')
    plt.plot(
        np.linspace(xMax[0], xMax[3], 100),
        polynomial(np.linspace(xMax[0], xMax[3], 100), fod, sod, tod)
    )
    plt.show()