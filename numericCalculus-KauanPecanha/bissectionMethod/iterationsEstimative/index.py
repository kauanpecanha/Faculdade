from math import log, ceil

# iterations estimating 

a = float(input("Entre com o primeiro número do intervalo: "))
b = float(input("Entre com o segundo número do intervalo: "))
epsilon = float(input('Entre com a tolerância desejada: '))
tol = 0
x = 0
aproxIterationsNumber = 0

aproxIterationsNumber = ((log(b-a) - log(epsilon))/(log(2)))

print(f'Aproximate number of iterations: {ceil(aproxIterationsNumber)}')