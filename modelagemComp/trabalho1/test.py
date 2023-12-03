from index import xArr, yArr
import numpy as np

def getVandermonde(x):
    v = []
    for i in range(len(x)):
        v.append([1, x[i], x[i]**2, x[i]**3, x[i]**4, x[i]**5])
    # v.append([[1, x[i], x[i]**2, x[i]**3, x[i]**4, x[i]**5] for i in range(len(x))])
    return v

v = getVandermonde(xArr)

vt = np.transpose(v)

vtv = vt @ v

# inv = np.linalg.inv(vtv)

# vtv_1_vt = inv @ vt

# result = vtv_1_vt @ v

print(vtv)

# # from test import vtv

# def getVandermonde(x):
#     v = []
#     for i in range(len(x)):
#         v.append([1, x[i], x[i]**2, x[i]**3, x[i]**4, x[i]**5])
#     # v.append([[1, x[i], x[i]**2, x[i]**3, x[i]**4, x[i]**5] for i in range(len(x))])
#     return v

# v = getVandermonde(xArr)

# vt = np.transpose(v)

# vtv = vt @ v

# # print(xArr)
# # print(yArr)

# x2Arr = [xArr[i]**2 for i in range(len(xArr))]
# x3Arr = [xArr[i]**3 for i in range(len(xArr))]
# x4Arr = [xArr[i]**4 for i in range(len(xArr))]
# x5Arr = [xArr[i]**5 for i in range(len(xArr))]
# x6Arr = [xArr[i]**6 for i in range(len(xArr))]
# x7Arr = [xArr[i]**7 for i in range(len(xArr))]


# x_sum = sum(xArr)
# x2_sum = sum(x2Arr)
# x3_sum = sum(x3Arr)
# x4_sum = sum(x4Arr)
# x5_sum = sum(x5Arr)
# x6_sum = sum(x6Arr)
# x7_sum = sum(x7Arr)

# # print(x_sum)
# # print(x2_sum)
# # print(x3_sum)
# # print(x4_sum)
# # print(x5_sum)
# # print(x6_sum)
# # print(x7_sum)

# a0 = 0
# a1 = 0
# a2 = 0
# a3 = 0
# a4 = 0
# a5 = 0

# y_sum = sum(yArr)
# xy_sum = [xArr[i] * yArr[i] for i in range(len(xArr))]
# x2y_sum = [(xArr[i]**2) * yArr[i] for i in range(len(xArr))]
# x3y_sum = [(xArr[i]**3) * yArr[i] for i in range(len(xArr))]
# x4y_sum = [(xArr[i]**4) * yArr[i] for i in range(len(xArr))]
# x5y_sum = [(xArr[i]**5) * yArr[i] for i in range(len(xArr))]

# A = [[len(xArr), x_sum, x2_sum],
#      [x_sum, x2_sum, x3_sum],
#      [x2_sum, x3_sum, x4_sum],
#      [x3_sum, x4_sum, x5_sum],
#      [x4_sum, x5_sum, x6_sum],
#      [x5_sum, x6_sum, x7_sum],
#     ]

# B = [
#     [y_sum],
#     [xy_sum],
#     [x2y_sum],
#     [x3y_sum],
#     [x4y_sum],
#     [x5y_sum],
# ]

# # fazer a matriz de vandermonde
# x = np.linalg.solve(vtv, B)