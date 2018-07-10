from sympy import *
x1, x2, t0 = symbols('x1 x2 t0')
y = 5*x1**2+x2**2-x1*x2+x1
x0 = [1.5, 1]
eps1 = 0.1
eps2 = 0.1
M = 10
grad = [diff(y, x1), diff(y, x2)]
k= 0
while k < M:
    finiteGrad = [limit(limit(grad[0], x1, x0[0]), x2, x0[1]),
                  limit(limit(grad[1], x1, x0[0]), x2, x0[1])]
    if (finiteGrad[0]**2+finiteGrad[1]**2)**0.5 > eps1:
            xNext = [x0[0]-t0*finiteGrad[0], x0[1]-t0*finiteGrad[1]]
            fi = limit(limit(y, x1,xNext[0]), x2, xNext[1])
            if diff(fi, t0, t0) > 0:
                DfiDt0 = diff(fi,t0)
                a = limit(DfiDt0,t0,0)*-1
                b = diff(DfiDt0,t0)
                t0Const = a/b
                xNext =[limit(xNext[0],t0,t0Const),limit(xNext[1],t0,t0Const)]
                if ((xNext[0]-x0[0])**2+(xNext[1]-x0[1])**2)**0.5>eps2:
                    x0=xNext
                    k+=1
                else:
                    answer = limit(limit(y,x1,xNext[0]),x2,xNext[1])
                    print('f(x)=',answer)
                    print('xmin=',xNext)
                    break
            else:
                answer = limit(limit(y,x1,xNext[0]),x2,xNext[1])
                print('Otvet=',answer)
                print('xmin=', xNext)
                break
    else:
        answer = limit(limit(y, x1, xNext[0]), x2, xNext[1])
        print('Otvet=', answer)
        print('xmin=', xNext)
        break










