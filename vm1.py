import numpy as np

eps = 0.001
a = np.array([[2, 1, 1], [1, 2, 1], [1, 1, 2]], "f")
n = 4
yk = np.array([1, 1, 1], "f")
xk = yk/np.linalg.norm(yk)
lk = [0, 0, 0]
lkp1 = []
k = 0
while True:

   ykp1 = np.dot(np.linalg.matrix_power(a, n),xk)
   k+=n
   xkp1 = ykp1 / np.linalg.norm(ykp1)
   for i in range(len(ykp1)):
       if float(xk[i]) > 0:
           lkp1.append(ykp1[i]/xk[i])

   s1=0
   s2=0
   for i in range(len(lkp1)):
       s1 += lkp1[i]
   s1 = s1 / len(lkp1)

   for i in range(len(lk)):
       s2 += lk[i]
   s2 = s2 / len(lk)

   if np.abs(s2-s1) < eps  :
       break

   xk = xkp1
   yk = ykp1
   lk = lkp1
   lkp1 = []
print(xk)
print(k)