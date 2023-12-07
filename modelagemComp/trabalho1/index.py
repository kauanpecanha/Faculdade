import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from data import xArr, yArr, beta, interval, y_interval, cost, sellingValue1, sellingValue2, sellingValue3, yf
from functions import solveMatrix, function, plotGraphic, setInterval, linearModel

while(True):
    # 
    print("\n\n\t\t Trabalho de Modelagem Computacional \t\t\n\n")
    
    # Input que permite o usuário escolher qual dos gráficos deseja visualizar
    option = int(input("Entre com uma das opções a seguir, para ver os gráficos deste software:\n 1 - Dados iniciais\n 2 - Modelo Linear\n 3 - Previsão de Compra e Venda\n 4 - Gráfico Total\n 5 - Finalizar Programa\n\n Opção Escolhida: "))
    
    # Estrutura condicional que garante que o usuário escolha uma das opções permitidas
    if option > 0 and option < 5:
        
        # Input que permite o usuário optar por linhas de grid ou não
        option2 = int(input("\nDeseja ativar as linhas de grid?\n 1 - Sim\n 0 - Não\n\n Opção desejada: "))
        
        if option2 == 1:
            
            # Plotagem do gráfico com as linhas de grid
            plotGraphic(xArr, yArr, beta, yf, interval, y_interval, option, True)
        
        elif option2 == 0:
            
            # Plotagem do gráfico sem as linhas de grid
            plotGraphic(xArr, yArr, beta, yf, interval, y_interval, option, False)
                    
    # Opção que encerra o loop de execução
    elif(option == 5):
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
print("\n\nFeito por:\n\n\t Kauan Peçanha Lira - Engenharia de Computação - 202110048911\n\t Fellipe de Sá Moraes - Engenharia Mecânica - Matrícula\n\t Julia Fontenla - Engenharia Mecânica - Matrícula\n\n")