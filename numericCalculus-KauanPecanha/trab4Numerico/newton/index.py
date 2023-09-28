import matplotlib.pyplot as plt

def dif_div_ordem(x, y): #Aqui sao realizadas as contas referentes a diferencas divididas de cada ordem (1 a 5, neste caso)
    coefs = [0.0, 0.0, 0.0, 0.0, 0.0]
    ddo1 = [0.0,0.0,0.0,0.0,0.0] #diferenca dividida de ordem 1
    ddo1[0] = (y[1]-y[0])/(x[1]-x[0])
    ddo1[1] = (y[2]-y[1])/(x[2]-x[1])
    ddo1[2] = (y[3]-y[2])/(x[3]-x[2])
    ddo1[3] = (y[4]-y[3])/(x[4]-x[3])
    ddo1[4] = (y[5]-y[4])/(x[5]-x[4])
    a1 = ddo1[0] #coeficiente a1 que vai para o polinomio de newton
    ddo2 = [0.0,0.0,0.0,0.0] #diferenca dividida de ordem 2
    ddo2[0] = (ddo1[1]-ddo1[0])/(x[2]-x[0])
    ddo2[1] = (ddo1[2]-ddo1[1])/(x[3]-x[1])
    ddo2[2] = (ddo1[3]-ddo1[2])/(x[4]-x[2])
    ddo2[3] = (ddo1[4]-ddo1[3])/(x[5]-x[3])
    a2 = ddo2[0] #coeficiente a2 que vai para o polinomio de newton
    ddo3 = [0.0,0.0,0.0] #diferenca dividida de ordem 3
    ddo3[0] = (ddo2[1]-ddo2[0])/(x[3]-x[0])
    ddo3[1] = (ddo2[2]-ddo2[1])/(x[4]-x[1])
    ddo3[2] = (ddo2[3]-ddo2[2])/(x[5]-x[2])
    a3 = ddo3[0] #coeficiente a3 que vai para o polinomio de newton
    ddo4 = [0.0,0.0] #diferenca dividida de ordem 4
    ddo4[0] = (ddo3[1]-ddo3[0])/(x[4]-x[0])
    ddo4[1] = (ddo3[2]-ddo3[1])/(x[5]-x[1])
    a4 = ddo4[0] #coeficiente a4 que vai para o polinomio de newton
    ddo5 = [0.0] #diferenca dividida de ordem 5
    ddo5 = (ddo4[1]-ddo4[0])/(x[5]-x[0])
    a5 = ddo5 #coeficiente a5 que vai para o polinomio de newton
    coefs = [a1, a2, a3, a4, a5] #lista de coeficientes que sera usada para obter o polinomio de newton
    return coefs

"""Aqui eh feito o calculo de cada termo do polinomio de newton, ja substituindo o ponto,
e, em seguida, somamos todos os termos para obter o P5(x) e retornamos o valor."""
def polinomioNewton(coef, ponto, x, y):
    termo1 = coef[0]*(ponto - x[0])
    termo2 = coef[1]*(ponto - x[0])*(ponto - x[1])
    termo3 = coef[2]*(ponto - x[0])*(ponto - x[1])*(ponto - x[2])
    termo4 = coef[3]*(ponto - x[0])*(ponto - x[1])*(ponto - x[2])*(ponto - x[3])
    termo5 = coef[4]*(ponto - x[0])*(ponto - x[1])*(ponto - x[2])*(ponto - x[3])*(ponto - x[4])
    p5n = y[0] + termo1 + termo2 + termo3 + termo4 + termo5 #calculo para obter o valor do polinomio de newton, ja com o valor do ponto aplicado dentro dos termos.
    return p5n

#Para descobrir a distancia no ponto 15

x = [0, 3, 5, 8, 13, 17] #valores do tempo
y = [0, 261, 339, 645, 993, 999] #valores da distancia

coefs = [0.0, 0.0, 0.0, 0.0, 0.0]
coefs = dif_div_ordem(x, y) #chama a funcao para realizar a interpolacao
distancia_x = 15 #ponto dito na questao
distancia_Px = polinomioNewton(coefs, distancia_x, x, y) #valor encontrado depois de aplicado o ponto no polinomio
print(f"Os coeficientes do polinomio encontrados são: {coefs}")
print(f"A estimativa da posição do carro quando t = {distancia_x} é {distancia_Px:.2f}")

#plotagem dos graficos da interpolacao

plt.scatter(x,y)
plt.plot(x,y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Y(X)")

#Para descobrir a velocidade no ponto 15

x = [0, 3, 5, 8, 13, 17] #valores do tempo
y = [75, 77,62, 78, 72, 77] #valores da velocidade

coefs = dif_div_ordem(x, y) #chama a funcao para realizar a interpolacao
velocidade_x = 15 #ponto dito na questao
velocidade_Px = polinomioNewton(coefs, velocidade_x, x, y) #valor encontrado depois de aplicado o ponto do polinomio
print(f"\n\nOs coeficientes do polinomio encontrados são: {coefs}")
print(f"A estimativa da sua velocidade quando t = {velocidade_x} é {velocidade_Px:.2f}")

#plotagem dos graficos da interpolacao

plt.scatter(x,y)
plt.plot(x,y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Y(X)")

plt.tight_layout()
plt.show()
