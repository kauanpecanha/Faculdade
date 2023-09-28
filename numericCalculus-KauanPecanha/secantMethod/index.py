a = float(input('Entre com o primeiro número do intervalo: '))
b = float(input('Entre com o segundo número do intervalo: '))
tol = float(input('Entre com a tolerância: '))
x0 = float(input('Entre com o valor de Xn-2: '))
x1 = float(input('Entre com o valor de Xn-1: '))

x = 0
iteration = 0

def f(x):
    return ((x**3) - 2*(x**2) - 5)# equação

def Xn(Xn_2, Xn_1):
    return ((Xn_1) - ((f(Xn_1)) * (((Xn_1) - (Xn_2))/((f(Xn_1)) - (f(Xn_2))))))

if( f(a) * f(b) < 0):
    
    while(True):
        
        x = Xn(x0, x1) # 2.3125

        print(f'k = {iteration} ; Xn-2 = {x0:.4f} ; Xn-1 = {x1:.4f} ; Xn = {x:.4f} ; f({x:.4f}) = {f(x):.4f} ; f({x1:.4f}) = {f(x1):.4f} ; f({x0:.4f}) = {f(x0):.4f}')

        if( abs(f(x)) < tol ): # 3.3288 > 0.01
            print(f'\nO módulo aproximado da raiz desta equação, neste intervalo, é de {x}, encontrado na iteração {iteration}')
            break

        x0 = x1
        x1 = x

        iteration+=1

else:
    print('Não há raízes reais neste intervalo.')