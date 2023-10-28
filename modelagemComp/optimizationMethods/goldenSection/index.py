# método da razão áurea - otimização
import numpy as np
from math import *

fiboNumber = ((sqrt(5) - 1)/2)

def function(x):
    return(
        (2 * sin(x)) - (x**2/10)
    )

def execGoldenRatio(x_l, x_mi, iterations):
    
    best_estimative = 0
    best_f_estimative = 0
    
    # x_l = x esquerdo
    # x_mi = x direito
    
    for i in range(iterations):
        
        d = (fiboNumber)*(x_mi - x_l)
        x1 = x_l + d
        x2 = x_mi - d
        
        f_x1 = function(x1)
        f_x2 = function(x2)
        
        if(f_x1 > f_x2):
            # intervalo de xl a x2 pode ser eliminado, por não conter o máximo
            x_l = x2
            best_estimative = x2
            best_f_estimative = function(x2)
        else:
            # intervalo de x1 a x_mi pode ser eliminado, por não conter o máximo
            x_mi = x1
            best_estimative = x1
            best_f_estimative = function(x1)
        
        print(f"{i:.2f} \t {x_l:.2f} \t {function(x_l):.2f} \t {x2:.2f} \t {function(x2):.2f} \t {x1:.2f} \t {function(x1):.2f} \t {x_mi:.2f} \t {function(x_mi):.2f} \t {d:.2f}")
        x1 = x_l + fiboNumber*(x_mi - x_l)
        i+=1
        
    return best_estimative, best_f_estimative


# escopo de execução

maxPoint, f_maxPoint = execGoldenRatio(0, 4, 8)
print(f"\n\nO ponto máximo dessa função está estimado em: x = {maxPoint:.2f}, para f(x) = {f_maxPoint:.2f}")