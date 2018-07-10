from sympy import*
from math import*

eps1 = float(0.05)
eps2 = float(0.005)
eps3 = float(0.001)
s = float(0.0001)
x1 = symbols('x1')
x2 = symbols('x2')
func = sympify(5*x1*x1 + x2*x2 - x1*x2 + x1)

#print('Введите М')
m = 100

x0 = [1.5,1]
x = [x0[i] for i in range(2)]

grad = []
for i in range(2):
    grad.append(1)
k = 0
while True:
    k = k+1
    #print('k',k)
    x0 = [x[i] for i in range(2)]
    grad[0] = (diff(func,x1)).subs(x1,x0[0]).subs(x2,x0[1])
    grad[1] = (diff(func,x2)).subs(x1,x0[0]).subs(x2,x0[1])
    norm = sqrt(sum([pow(grad[i],2) for i in range(2)]))
    #print('norm1',norm)
    if norm < eps1:
        x = [x0[i] for i in range(2)]
        break
    else:
        if k >= m:
            x = [x0[i] for i in range(2)]
            break
        else:
            a = 0
            b = 1
            t = symbols('t')
            fi = sympify(func.subs(x1,x0[0]-t*grad[0]).subs(x2,x0[1]-t*grad[1]))
            q = 0
            while (abs(fi.subs(t,a)- fi.subs(t,b))> eps3):
                w = (a + b)/2
                q = q+1
                if fi.subs(t,w - s)< fi.subs(t,w + s):
                    b = w + s
                if fi.subs(t,w - s)> fi.subs(t,w + s):
                    a = w - s
                tay = (a+b)/2
            print('t',tay)
            print('x0',x0)
            for i in range(2):
                x[i] = x0[i] - tay*grad[i]
            norm = sqrt(sum([pow(x[i]-x0[i],2) for i in range(2)]))
            modul = abs(func.subs(x1,x[0]).subs(x2,x[1])-func.subs(x1,x0[0]).subs(x2,x0[1]))
            #print('norm',norm)
            #print('module',modul)
    if (norm < eps2)and(modul < eps2):
        break
print('k',k)
print('x =',x)
print('func =',func.subs(x1,x[0]).subs(x2,x[1]))
#Пантелеев - 185 стр    
    

 
            
