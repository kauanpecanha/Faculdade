import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from data import xArr, yArr, beta, interval, y_interval, cost, sellingValue1, sellingValue2, sellingValue3, yf
from functions import solveMatrix, function, plotGraphic, setInterval, linearModel

while(True):
    print("\n\n\t\t Trabalho de Modelagem Computacional \t\t\n\n")
    
    option = int(input("Entre com uma das opções a seguir, para ver os gráficos deste software:\n 1 - Dados iniciais\n 2 - Modelo Linear\n 3 - Previsão de Compra e Venda\n 4 - Gráfico Total\n 5 - Finalizar Programa\n\n Opção Escolhida: "))
    
    if option > 0 and option < 5:
        
        option2 = int(input("\nDeseja ativar as linhas de grid?\n 1 - Sim\n 0 - Não\n\n Opção desejada: "))
        
        if option2 == 1:
            
            plotGraphic(xArr, yArr, beta, yf, interval, y_interval, option, True)
        
        elif option2 == 0:
            
            plotGraphic(xArr, yArr, beta, yf, interval, y_interval, option, False)
        
        else:
            
            plotGraphic(xArr, yArr, beta, yf, interval, y_interval, option, True)
            
            
        
    elif(option == 5):
        print("\n\n Programa finalizado.\n\n")
        break
    else:
        print("Entre com uma opção válida")

# ------------------------------------------------------------------------------------------------------------------------

# Resposta: Quando o preço das ações é de, aproximadamente, R$4,50

# Qual seria o lucro (ou prejuízo) do investidor, caso as ações fossem vendidas considerando-se os cenários:
    # a) Cinco meses após a compra;
    # a) Oito meses após a compra;
    # a) Doze meses após a compra;
    
    
# ------------------ Desenvolvimento ----------------------------
# 1000 ações compradas quando t = 4 anos

print("-"*40 + " RELATÓRIO " + "-"*40)

# Impressão das informações de compra
print(f"\n\nCOMPRA\n\nO valor de compra da ação quando t = 4 anos é: R${cost:.2f}")

# impressão das informações de venda
print(f"\n\nVENDA\n\nO valor que ele conseguiria através da venda das ações estão listados abaixo:\n\ta) Cinco meses após a compra: R${sellingValue1[0]:.2f}\n\tb) Oito meses após a compra: R${sellingValue2[0]:.2f}\n\tc) Doze meses após a compra: R${sellingValue3[0]:.2f}")

# impressão das informações de lucro
print(f"\n\nLUCRO\n\nOs valores de lucro são listados abaixo:\n\ta) Cinco meses após a compra: R${(sellingValue1[0] - cost):.2f}\n\tb) Oito meses após a compra: R${(sellingValue2[0] - cost):.2f}\n\tc) Doze meses após a compra: R${(sellingValue3[0] - cost):.2f}\n\n\n")