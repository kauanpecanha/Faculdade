from math import pi, sqrt, exp, e
import numpy as np
import matplotlib.pyplot as plt

def normalDist(x, mi, sigma):
    return (
        ((1)/(sigma) * (sqrt(2*pi)))
        *
        (e**((-1/2)*(((x - mi)/(sigma))**2)))
    )

xArray = np.array([5, 5, 10, 10, 10, 20, 20, 25, 25])
yArray = np.array([30, 29, 28, 33, 31, 25, 22, 20, 19])


def sum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum

def media(arr):
    summ = sum(arr)
    return summ/len(arr)

def sumBoth(xArr, yArr):
    arr = []
    for i in range(len(xArr)):
        arr.append((xArr[i])*(yArr[i]))
    
    return sum(arr)

def squareSummatory(arr):
    sum = 0
    for i in range(len(arr)):
        sum += (arr[i]**2)
    return sum

def sumDeltas(arr, med, id):
    if(id == 1):
        sum = 0
        for i in range(len(arr)):
            sum += arr[i] - med
        return sum
    else:
        sum = 0
        for i in range(len(arr)):
            sum += ((arr[i] - med)**2)
        return sum

def beta1(sumXiYi, sumYi, sumXi, sumXiSquare, squareSumXi, size):
    return(
        ((sumXiYi) - ((1/size)*(sumXi)*(sumYi)))
        /
        (sumXiSquare - ((1/size)*(squareSumXi)))
    )

def beta0(size, sumYi, sumXi, beta1):
    return(
        (((1/size)*(sumYi)) - ((1/size)*(beta1)*(sumXi)))
    )

# plt.scatter(xArray, yArray)
# plt.show()

print(f"A média de x é: {media(xArray):.2f}")
print(f"A média de y é: {media(yArray):.2f}")
print(f"A soma de todos os x é: {sum(xArray):.2f}")
print(f"A soma de todos os y é: {sum(yArray):.2f}")

print(f"O somatório de XiYi é igual a: {sumBoth(xArray, yArray):.2f}")
print(f"O quadrado do somatório de xi é igual a: {((sum(xArray))**2):.2f}")
print(f"O somatório de xi ao quadrado é: {squareSummatory(xArray):.2f}")

print(f"O somatório da diferença de xi por xmed é: {sumDeltas(xArray, media(xArray), 1):.2f}")
print(f"O somatório da diferença de yi por ymed é: {sumDeltas(yArray, media(yArray), 1):.2f}")
print(f"O somatório dos quadrados das diferenças de xi por xmed é: {sumDeltas(xArray, media(xArray), 2)}")
print(f"O somatório dos quadrados das diferenças de yi por ymed é: {sumDeltas(yArray, media(yArray), 2)}")

sumXiYi = sumBoth(xArray, yArray)
sumYi = sum(yArray)
sumXi = sum(xArray)
summatoryXsquare = squareSummatory(xArray)
squareSummatoryX = sum(xArray)**2
size = len(xArray)
b1 = beta1(sumXiYi, sumYi, sumXi, summatoryXsquare, squareSummatoryX, size)
b0 = beta0(size, sumYi, sumXi, b1)

def function(beta0, beta1, xIn):
    return beta0 + beta1 * xIn

print(f"O valor de b1 é igual a: {b1:.2f}")
print(f"O valor de b0 = {b0:.2f}")

xInterval = np.linspace(0, 30, 1000)

plt.grid()
plt.scatter(xArray, yArray)
plt.plot(xInterval, function(b0, b1, xInterval))
plt.show()