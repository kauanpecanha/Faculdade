import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from data import xArr, yArr, beta, interval, y_interval, cost, sellingValue1, sellingValue2, sellingValue3, yf, beta
from functions import solveMatrix, function, plotGraphic, setInterval, linearModel

while(True):
    # 
    print("\n\n\t\t Trabalho de Modelagem Computacional \t\t\n\n")
    
    # Input que permite o usuário escolher qual dos gráficos deseja visualizar
    option = int(input("Entre com uma das opções a seguir, para ver os gráficos deste software:\n 1 - Dados iniciais\n 2 - Modelo Linear (com dados iniciais)\n 3 - Modelo Linear (s/ dados iniciais)\n 4 - Previsão de Compra e Venda até 4 meses após a compra\n 5 - Previsão de Compra e Venda até 8 meses após a compra\n 6 - Previsão de Compra e Venda até 12 meses após a compra\n 7 - Gráfico Total (c/ os pontos)\n 8 - Gráfico Total (s/ os pontos)\n 9 - Função que descreve a regressão Polinomial\n 10 - Finalizar Programa\n\n Opção Escolhida: "))
    
    # Estrutura condicional que garante que o usuário escolha uma das opções permitidas
    if option > 0 and option <= 8:
        
        # Input que permite o usuário optar por linhas de grid ou não
        option2 = int(input("\nDeseja ativar as linhas de grid?\n 1 - Sim\n 0 - Não\n\n Opção desejada: "))
        
        if option2 == 1:
            
            # Plotagem do gráfico com as linhas de grid
            plotGraphic(xArr, yArr, beta, yf, interval, y_interval, option, True)
        
        elif option2 == 0:
            
            # Plotagem do gráfico sem as linhas de grid
            plotGraphic(xArr, yArr, beta, yf, interval, y_interval, option, False)
                    
    elif(option == 9):
        print("\n\n Impressão da Função de Regressão Polinomial \n\n")
        
        print(f"{float(beta[0]):.2f} * x ** 0 + {float(beta[1]):.2f} * x ** 1+ {float(beta[2]):.2f} * x ** 2 + {float(beta[3]):.2f} * x ** 3 + {float(beta[4]):.2f} * x ** 4 + {float(beta[5]):.2f} * x ** 5")
        
    
    # Opção que encerra o loop de execução
    elif(option == 10):
        print("\n\n Programa finalizado.\n\n")
        
        # Encerramento do loop de execução
        break
    
    else:
        print("Entre com uma opção válida")

# Impressão com o intuito de organizar as informações finais, no terminal do usuário
print("-"*40 + " RELATÓRIO " + "-"*40)

# Impressão das informações de compra
print(f"\n\nCOMPRA\n\nO valor de compra da ação quando t = 4 anos é: R${cost:.2f}")

# impressão das informações de venda
print(f"\n\nVENDA\n\nO valor que ele conseguiria através da venda das ações estão listados abaixo:\n\ta) Cinco meses após a compra: R${sellingValue1[0]:.2f}\n\tb) Oito meses após a compra: R${sellingValue2[0]:.2f}\n\tc) Doze meses após a compra: R${sellingValue3[0]:.2f}")

# impressão das informações de lucro
print(f"\n\nLUCRO\n\nOs valores de lucro são listados abaixo:\n\ta) Cinco meses após a compra: R${(sellingValue1[0] - cost):.2f}\n\tb) Oito meses após a compra: R${(sellingValue2[0] - cost):.2f}\n\tc) Doze meses após a compra: R${(sellingValue3[0] - cost):.2f}\n\n\n")

print("-"*40 + " Trabalho de Modelagem Computacional " + "-"*40)
print("\n\nFeito por:\n\n\t Kauan Peçanha Lira - Engenharia de Computação - 202110048911\n\t Fellipe de Sá Moraes - Engenharia Mecânica - 202110064311\n\t Julia Fontenla - Engenharia Mecânica - 202110065511\n\n")