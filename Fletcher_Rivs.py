from sympy import *
x1, x2, t0 = symbols('x1 x2 t0')
y = 8*x1**2+x2**2-x1*x2+x1
x0 = [1, 2]
eps1 = 0.1
eps2 = 0.15
M = 10
k = 0
while k < M:
    grad = [diff(y, x1), diff(y, x2)]
    finiteGrad = [limit(limit(grad[0], x1, x0[0]), x2, x0[1]),
                  limit(limit(grad[1], x1, x0[0]), x2, x0[1])]
    if (finiteGrad[0] ** 2 + finiteGrad[1] ** 2) ** 0.5 > eps1:
        if k==0:
            d0=[-1*finiteGrad[0],-1*finiteGrad[1]]
            d0Prev = d0
        if k%2==0:
            beta = 0
        else:
            finiteGradPrev = [limit(limit(grad[0], x1, xPrev[0]), x2, xPrev[1]),
                              limit(limit(grad[1], x1, xPrev[0]), x2, xPrev[1])]
            beta = ((finiteGrad[0]**2+finiteGrad[1]**2))/\
                       ((finiteGradPrev[0]**2+finiteGradPrev[1]**2))

        d0 = [-1*finiteGrad[0]+beta*d0Prev[0],-1*finiteGrad[1]+beta*d0Prev[1]]
        xNext = [x0[0] + t0 * d0[0],x0[1] + t0 * d0[1]]
        fi = limit(limit(y,x1,xNext[0]),x2,xNext[1])
        DfiDt0 = diff(fi,t0)
        a = limit(DfiDt0, t0, 0) * -1
        b = diff(DfiDt0, t0)
        t0Const = a / b
        xNext = [limit(xNext[0],t0,t0Const),
                 limit(xNext[1],t0,t0Const)]
        temp = [xNext[0]-x0[0],xNext[1]-x0[1]]
        if ((temp[0]**2+temp[1]**2)>eps2) and\
                (abs(limit(limit(y,x1,xNext[0]),x2,xNext[1])-limit(limit(y,x1,x0[0]),x2,x0[1]))>eps2):
                k += 1
                xPrev = x0
                d0Prev = d0
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
