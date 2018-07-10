from rawson import *
r = 1
c = 2
lm = 0.3
mu = 0.2
x1,x2 = symbols('x1 x2')
y = 8*x1**2+x2**2-x1*x2+x1
#y = 5*x1**2+x2**2-x1*x2+x1
g = x1+x2
#g = x1+x2-1
ravenstvo = False
x0 = [1.5,2]
eps1 = 0.007
eps2 = 0.006
eps3 = 0.01
k = 0
m = 500
while k < m:
    if ravenstvo:
        p = r / 2 * g ** 2 + lm*g
    else:
        p = lm*g + 1/(2*r)*((max(0,mu+r*limit(limit(g,x1,x0[0]),x2,x0[1])))**2-mu**2)
    F = y + p

    minimum = minimumRawson(F,x0,eps1,eps2)
    print(minimum)
    if abs(limit(limit(p,x1,minimum[0]),x2,minimum[1]))>eps3:
        lm = lm + r * limit(limit(g, x1, minimum[0]), x2, minimum[1])
        mu = max(0, mu+r*limit(limit(g, x1, minimum[0]), x2,minimum[1]))
        #print(lm)
        r *= c
        k += 1
        x0 = minimum
    else:
        print('Ответ',minimum)
        print('k =',k)
        break