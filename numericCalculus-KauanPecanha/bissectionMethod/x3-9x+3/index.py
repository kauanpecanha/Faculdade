
# método da bisseção

# importação das bibliotecas

# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

tol = 0
x = 0
iteration = 0

def setXn(k, l):
    return ((k+l)/(2))

def f(x):
    return # the function comes here

def setTol(i, j):
    return (abs(j - i))


a = float(input("Entre com o primeiro número do intervalo: "))
b = float(input("Entre com o segundo número do intervalo: "))
epsilon = float(input('Entre com a tolerância desejada: '))

a_zero = a
b_zero = b

tol = setTol(a, b)

while(tol>epsilon):
    x = setXn(a, b)

    f_a = f(a)
    f_B = f(b)
    f_x = f(x)

    if((f_a)*(f_x)<0):
        b = x
    else:
        a = x
    
    tol = setTol(a, b)

    print(f'ITERATION {iteration} - Range of possible solutions: [{a:.4f}, {b:.4f}], near {x:.4f}')

    iteration+=1


xf = np.linspace(a-1, b+1, 100)
yf = xf**3 - 9*xf + 3

plt.grid()
plt.scatter(a, f(a), c='blue')
plt.scatter(b, f(b), c='blue')
plt.scatter(a_zero, f(a_zero), c='red')
plt.scatter(b_zero, f(b_zero), c='red', label='Função x³-9x+3')
plt.plot(xf, yf, c='purple')



print(f'Range of possible solutions: [{a:.4f}, {b:.4f}], near {x:.4f}')
print(f'Total of iterations: {iteration}')