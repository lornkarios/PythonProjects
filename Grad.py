import math


def func(x, y):
    return x*x + 5*y - 2


def norm(gfp1):
    return math.sqrt(gfp1[0]*gfp1[0] + gfp1[1]*gfp1[1])


def proizv(x, y, i):
    dx = 0.00000001
    if i == 1:
        return (func(x+dx, y)-func(x, y))/dx
    elif i == 2:
        return (func(x, y+dx)-func(x, y))/dx


M = 15
xk = [0, 0]
xkp1 = xk
eps = 0.002
eps1 = 0.003
eps2 = 0.0004
gf = [proizv(xk[0], xk[1], 1), proizv(xk[0], xk[1], 2)]
k = 0
x = xk
xz = xk
while True:
    gfp1 = [proizv(xk[0], xk[1], 1), proizv(xk[0], xk[1], 2)]
    if (norm(gfp1) < eps1)or(k >= M):
        xz = xk
        break
    while True:
        tk = 0.2
        xkp1[0] = xk[0] - tk*gfp1[0]
        xkp1[1] = xk[1] - tk * gfp1[1]
        if func(xkp1[0], xkp1[1]) - func(xk[0], xk[1]) < 0 :
            break
        else:
            tk = tk/2
    x[0] = xkp1[0]-xk[0]
    x[1] = xkp1[1]-xk[1]
    if (norm(x) < eps2) or (func(xkp1[0], xkp1[1]) - func(xk[0], xk[1])):
        xz = xkp1
        break

print(xz)