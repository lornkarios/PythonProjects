from rawson import *
r = 2
c = 2
x1,x2 = symbols('x1 x2')
#y = 5*x1**2+x2**2-x1*x2+x1
y = 8*x1**2+x2**2-x1*x2+x1
#g = x1+x2-1
g = 2*x1+x2-3
ravenstvo = True
x0 = [1,2]
eps1 = 0.07
eps2 = 0.06
eps3 = 0.05
k = 0
m = 500
while k < m:
    if ravenstvo:
        p = r / 2 * g ** 2
    else:
        p = r/2 * (max((limit(limit(g,x1,x0[0]),x2,x0[1])),0))**2
    F = y + p
    minimum = minimumRawson(F,x0,eps1,eps2)
    if abs(limit(limit(p,x1,minimum[0]),x2,minimum[1]))>eps3:
        r *= c
        k += 1
        x0 = minimum
    else:
        print('Ответ ',minimum)
        print('k =',k)
        break