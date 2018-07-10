from sympy import *
import numpy as np


def is_pos_def(x):
    return np.all(np.linalg.eigvals(x) > 0)


def matrix_obrat(mat):
    matNP = np.array(mat)
    matNP = matNP.transpose()
    opredelitel = np.linalg.det(mat)
    temp0 = mat
    for i in range(len(mat)):
        for j in range(len(mat)):
            temp = matNP
            temp = np.delete(temp,i,0)
            temp = np.delete(temp,j,1)
            det = np.linalg.det(temp)
            temp0[i][j] = (det * (-1)**(i+j))/opredelitel
    return temp0


x1, x2, t0 = symbols('x1 x2 t0')
y = 8*x1**2+x2**2-x1*x2+x1
x0 = [1, 2]
eps1 = 0.1
eps2 = 0.15
M = 10
gesse = [[0,0],[0,0]]
gesse[0][0] = float(diff(y,x1,x1))
gesse[1][1] = float(diff(y,x2,x2))
gesse[0][1] = float(diff(y,x2,x1))
gesse[1][0] = float(diff(y,x2,x1))
k = 0
gesse_obratnaya = [[0, 0], [0, 0]]
while k < M:
    grad = [diff(y, x1), diff(y, x2)]
    finiteGrad = [limit(limit(grad[0], x1, x0[0]), x2, x0[1]),
                  limit(limit(grad[1], x1, x0[0]), x2, x0[1])]
    if (finiteGrad[0] ** 2 + finiteGrad[1] ** 2) ** 0.5 > eps1:
        gesse_obratnaya = matrix_obrat(gesse)
        if is_pos_def(gesse_obratnaya) :
            d0 = -1 * (np.dot(gesse_obratnaya, finiteGrad))
        else:
            d0 = -1 * finiteGrad
        print(t0)
        xNext = x0+t0*d0
        fi = limit(limit(y,x1,xNext[0]),x2,xNext[1])
        DfiDt0 = diff(fi,t0)
        a = limit(DfiDt0, t0, 0) * -1
        b = diff(DfiDt0, t0)
        t0Const = a / b
        xNext[0] = limit(xNext[0],t0,t0Const)
        xNext[1] = limit(xNext[1],t0,t0Const)
        temp = xNext-x0

        if ((temp[0]**2+temp[1]**2)>eps2) and\
            (abs(limit(limit(y,x1,xNext[0]),x2,xNext[1])-limit(limit(y,x1,x0[0]),x2,x0[1]))>eps2):
            k += 1
            x0 = xNext
        else:
            answer = limit(limit(y, x1, xNext[0]), x2, xNext[1])
            print('f(x)=', answer)
            print('xmin=', xNext)
            break
    else:
        answer = limit(limit(y, x1, xNext[0]), x2, xNext[1])
        print('f(x)=', answer)
        print('xmin=', xNext)
        break



