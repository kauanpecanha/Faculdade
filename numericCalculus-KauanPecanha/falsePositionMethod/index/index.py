
# método da falsa posição

a = float(input("Entre com o primeiro número do intervalo: "))
b = float(input("Entre com o segundo número do intervalo: "))
epsilon = float(input('Entre com a tolerância desejada: '))

x = 0
iteration = 0

def f(x):
    return # the function goes here

def setXn(k, l):
    return ( # esta sintaxe visa melhorar a visualização dos parâmetros - este parênteses determina o resultado como um todo
            
                ((k * (f(l))) - (l * (f(k)))) # numerador da fração
                /
                ((f(l) - f(k))) # denominador da fração

            )

x = setXn(a, b)

if((f(a) * f(b)) < 0):
    
    while(f(x) >= epsilon):
    
        x = setXn(a, b)

        if(f(a) * f(x) < 0):
            b = x
        else:
            a = x
    
        iteration += 1
else:
    print('Não há raízes reais neste intervalo.')

print(f'A raiz aproximada dessa função é {x}, se encontra no intervalo [{a}, {b}], e foi encontrado após {iteration} iterações.')