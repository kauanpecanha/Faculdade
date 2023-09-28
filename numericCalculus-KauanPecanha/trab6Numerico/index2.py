import matplotlib.pyplot as plt

def ordem_delta(y):
    delta1 = [0.0, 0.0, 0.0]
    delta1[0] = y[1]-y[0]
    delta1[1] = y[2]-y[1]
    delta1[2] = y[3]-y[2]
    a1 = delta1[0]
    delta2 = [0.0, 0.0]
    delta2[0] = delta1[1]-delta1[0]
    delta2[1] = delta1[2]-delta1[1]
    a2 = delta2[0]
    a3 = delta2[1]-delta2[0]
    delta = [a1, a2, a3]
    return delta

def calculo_polinomio(y, z, delta):
    termo1 = z*delta[0]
    termo2 = (z*(z-1)*delta[1])/2
    termo3 = (z*(z-1)*(z-2)*delta[2])/6
    polinomio = y[0] + termo1 + termo2 + termo3
    return polinomio

x = [136, 178, 220, 262]
y = [15, 50, 66, 76]
#descobrindo h
h = x[1]-x[0]
x0 = 200
#descobrindo z
z = (x0 - x[0])/h
#fazendo a parte da tabela
coef_delta = []
coef_delta = ordem_delta(y)
#descobrindo o valor do polinomio
p_x = calculo_polinomio(y, z, coef_delta)

print(f"O valor encontrado de h eh: {h}")
print(f"O valor encontrado de z eh: {z:.2f}")
print(f"Os coeficientes delta n de y são: {coef_delta}")
print(f"O valor encontrado para p de {x0} eh: {p_x:.4f}C")

#plotagem dos graficos da interpolacao

plt.scatter(x,y)
plt.plot(x,y)
plt.xlabel("X em ppm")
plt.ylabel("Y em C")
plt.title("Grafico da relacao entre solubilidade e temperatura")

plt.tight_layout()
plt.show()
