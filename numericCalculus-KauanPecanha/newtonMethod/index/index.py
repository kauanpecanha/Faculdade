#método da bisseção

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return ((x**3) - (9*(x)) + 3)

def setXn(k, l):
    return ((k+l)/(2))

a = float(input("Entre com o primeiro número do intervalo: "))
b = float(input("Entre com o segundo número do intervalo: "))
epsilon = float(input('Entre com a tolerância desejada: '))
iteration = 0

plt.scatter(a, f(a), c='red')
plt.scatter(b, f(b), c='red')

if( f(a) * f(b) < 0 ):
  
  while(True):

    tol = abs( b - a )

    x = setXn(a, b)

    print(f'k = {iteration} ; a = {a:.4f} ; b = {b:.4f} ; x = {x:.4f} ; |Bn - An| = { tol } ; f({a:.4f}) = {f(a):.4f} ; f({b:.4f}) = {f(b):.4f} ; f({x:.4f}) = {f(x):.4f}')

    if( f(a) * f(x) < 0):
      
      b = x

    else:
      
      a = x
    
    if( tol < epsilon ):
      print(f'A raiz aproximada {x} foi encontrada na iteração {iteration}')
      break
    
    iteration+=1
  
  plt.grid()
  plt.scatter(x, f(x), c='blue')
  plt.plot(np.linspace(a-1, b+1, 1000), f(np.linspace(a-1, b+1, 1000)), c='purple')