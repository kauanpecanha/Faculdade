import numpy as np
from math import *

def function(x, y):
    # insert your function right here
    return (x*y**2)

def fx(x, y):
    # insert your function right here
    return (y**2)

def fxx(x, y):
    return 0

def fxy(x, y):
    return (2*y)

def fy(x, y):
    # insert your function right here
    return (2*x*y)

def fyy(x, y):
    return 2*x

def fyx(x, y):
    return (2)

# Cálculo do aclive máximo no ponto (2, 2)
x = 2
y = 2
value = function(x, y)
print(value)

parX = fx(x, y)
parY = fy(x, y)

print(f"{parX}, {parY}")
print(f"Gradiente: {parX}*i + {parY}*j")

hessMatrix = np.matrix([
    [fxx(x, y), fxy(x, y)],
    [fyx(x, y), fyy(x, y)]
])

det = np.linalg.det(hessMatrix)

print(f"O determinante é {det:.2f}")

if(det > 0 and fxx(x, y) > 0):
    print(f"O ponto({x}, {y}) é um mínimo local")
elif(det > 0 and fxx(x, y) < 0):
    print(f"O ponto({x}, {y}) é um máximo local")
else:
    print(f"O ponto({x}, {y}) é um ponto de sela")