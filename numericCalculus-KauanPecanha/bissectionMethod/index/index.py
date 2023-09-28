# método da bisseção

# importação das bibliotecas

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return ((x**3) - (9*(x)) + 3)

def setXn(k, l):
    return ((k+l)/(2))

def setTol(i, j):
    return (abs(j - i))

a = float(input("Entre com o primeiro número do intervalo: "))
b = float(input("Entre com o segundo número do intervalo: "))
epsilon = float(input('Entre com a tolerância desejada: '))

tol = abs(b - a)
x = 0
iteration = 0
xf = np.linspace(a-0.25, b+0.25, 100)
a_zero = a
b_zero = b

while(True):
  
  tol = setTol(a, b)

  if(tol>epsilon):
    
    x = setXn(a, b)

    print(f'ITERATION {iteration} - Range of possible solutions: [{a:.4f}, {b:.4f}], near {x:.4f}')
    
    if( f(a) * f(x) < 0):
        b = x
    else:
        a = x

    iteration+=1
  
  else:
    print(f'\nNúmero de iterações atingido: {iteration}\n')
    print(f'\nRaiz aproximada: {x}\n')
    break

plt.grid()
plt.scatter(a, f(a), c='blue')
plt.scatter(b, f(b), c='blue')
plt.scatter(a_zero, f(a_zero), c='red')
plt.scatter(b_zero, f(b_zero), c='red')

plt.scatter(x, f(x), c='yellow')
plt.plot(xf, f(xf), c='purple')

print('Aproximação final:')
print(f'Intervalo inicial: [{a_zero}, {b_zero}] ; Intervalo final: [{a}, {b}] ; raiz aproximada: {x}')
