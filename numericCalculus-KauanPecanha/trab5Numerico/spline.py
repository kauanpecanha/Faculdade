from sympy import symbols
import numpy as np
import matplotlib.pyplot as plt

# algoritmo de interpolação de spline

def f(x):
    if(-2<=x and x<=-1):
        return ((x+1)**3)
    elif(1<=x and x<=2):
        return ((x-1)**3)
    else:
        return 0

def s0(x):
    return(
        a[0] + b[0]*(x+2) + c[0]*(x+2)**2 + d[0]*(x+2)**3
    )
def s1(x):
    return(
        a[1] + b[1]*(x+1) + c[1]*(x+1)**2 + d[1]*(x+1)**3
    )
def s2(x):
    return(
        a[2] + b[2]*(x-1) + c[2]*(x-1)**2 + d[2]*(x-1)**3
    )

def showGraphic(x):
    for i in range(len(x)):
        plt.scatter(x[i], fx[i])

        plt.xlabel('Valores de X')
        plt.ylabel('Valores de Y')
        plt.plot(np.linspace(-2, -1, 100), s0(np.linspace(-2, -1, 100)))
        plt.plot(np.linspace(-1, 1, 100), s1(np.linspace(-1, 1, 100)))
        plt.plot(np.linspace(1, 2, 100), s2(np.linspace(1, 2, 100)))
        plt.grid()
        plt.show()

def s(x, y):

    a = [] # lista de coeficientes de a
    b = []
    d = []
    h = 1 # igualmente espaçados

    for i in range(0, len(y)):
        a.append(y[i]) # determinação dos coeficientes de a. Obs.: a3 não é parte de nenhuma equação de spline

    A = np.array([
            [1, 0, 0, 0],
            [h, 2*(h + h), h, 0],
            [0, h, 2*(h+h), h],
            [0, 0, 0, 1],
    ])

    B = np.array([
        [0],
        [((3/h)*(a[2] - a[1])) - ((3/h)*(a[1] - a[0]))],
        [((3/h)*(a[3] - a[2])) - ((3/h)*(a[2] - a[1]))],
        [0],
    ])

    c = np.linalg.solve(A, B) # determinação dos coeficientes c

    for i in range(0, 3): # determinação dos coeficientes b            
        b.append(
            float(((1/h)*(a[i+1] - a[i])) - ((h/3)*((2*c[i])+(c[i+1]))))
        )
    
    for i in range(0, 3): # determinação dos coeficientes d
        d.append(
            float((c[i+1] - c[i])/(3*h))
        )
    
    return a, b, c, d

x = [-2, -1, 1, 2]
fx = []

for i in x:
    fx.append(f(i))

a, b, c, d = s(x, fx)

print('\n\nOs polinômios podem ser vistos abaixo:\n')
print(f'S0(x) = {a[0]} + {(b[0]):.2f}(x+2) + {float(c[0])}(x+2)² + {(d[0]):.2f}(x+2)³ para x e [-2, -1]')
print(f'S1(x) = {a[1]} + {(b[1]):.2f}(x+1) + {float(c[1])}(x+1)² + {(d[1]):.2f}(x+1)³  para x e [-1, 1]')
print(f'S2(x) = {a[2]} + {(b[2]):.2f}(x-1) + {float(c[2])}(x-1)² + {(d[2]):.2f}(x-1)³  para x e [1, 2]')
print('\n\n')

showGraphic(x)