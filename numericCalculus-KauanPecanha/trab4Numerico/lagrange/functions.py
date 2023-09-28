import matplotlib.pyplot as plt
import numpy as np
from data import x, f_x

x0 = x[0]
x1 = x[1]
x2 = x[2]
x3 = x[3]
x4 = x[4]
x5 = x[5]


def defineL0(x0, x1, x2, x3, x4, x5, x):
    
    return(
        ((x-x1)*(x-x2)*(x-x3)*(x-x4)*(x-x5))
        /
        ((x0-x1)*(x0-x2)*(x0-x3)*(x0-x4)*(x0-x5))
    )

def defineL1(x0, x1, x2, x3, x4, x5, x):
    
    return(
        ((x-x0)*(x-x2)*(x-x3)*(x-x4)*(x-x5))/((x1-x0)*(x1-x2)*(x1-x3)*(x1-x4)*(x1-x5))
    )

def defineL2(x0, x1, x2, x3, x4, x5, x):
    
    return(
        ((x-x0)*(x-x1)*(x-x3)*(x-x4)*(x-x5))
        /
        ((x2-x0)*(x2-x1)*(x2-x3)*(x2-x4)*(x2-x5))
    )

def defineL3(x0, x1, x2, x3, x4, x5, x):
    
    return(
        ((x-x0)*(x-x1)*(x-x2)*(x-x4)*(x-x5))
        /
        ((x3-x0)*(x3-x1)*(x3-x2)*(x3-x4)*(x3-x5))
    )

def defineL4(x0, x1, x2, x3, x4, x5, x):
    
    return(
        ((x-x0)*(x-x1)*(x-x2)*(x-x3)*(x-x5))
        /
        ((x4-x0)*(x4-x1)*(x4-x2)*(x4-x3)*(x4-x5))
    )

def defineL5(x0, x1, x2, x3, x4, x5, x):
    
    return(
        ((x-x0)*(x-x1)*(x-x2)*(x-x3)*(x-x4))
        /
        ((x5-x0)*(x5-x1)*(x5-x2)*(x5-x3)*(x5-x4))
    )

def lagrange(x):
    l0 = defineL0(x0, x1, x2, x3, x4, x5, x)
    l1 = defineL1(x0, x1, x2, x3, x4, x5, x)
    l2 = defineL2(x0, x1, x2, x3, x4, x5, x)
    l3 = defineL3(x0, x1, x2, x3, x4, x5, x)
    l4 = defineL4(x0, x1, x2, x3, x4, x5, x)
    l5 = defineL5(x0, x1, x2, x3, x4, x5, x)

    result = (l0 * f_x[0]) + (l1 * f_x[1]) + (l2 * f_x[2]) + (l3 * f_x[3]) + (l4 * f_x[4]) + (l5 * f_x[5])

    return result