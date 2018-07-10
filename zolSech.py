import math
def func(x):
    return 2 * x * x - 2 * x + 2.5


def get_int(s1):
    while True:
            try:
                s = (int)(input(s1))
                return s
            except ValueError as err:
                print(err)


# a0 = get_int('a0= ')
# b0 = get_int('b0= ')

l = 0.5
a0 = -1
b0 = 9
k = 0
yk = a0 + (3-math.sqrt(5))/2 * (b0 - a0)
zk = a0 + b0 - yk
ak = a0
bk = b0
akp1 = 0
bkp1 = 0
ykp1 = 0
zkp1 = 0
delta = 1
while delta > l:
    k += 1
    if func(yk) <= func(zk):

            akp1 = ak
            bkp1 = zk
            ykp1 = akp1 + bkp1 - yk
            zkp1 = yk
    elif func(yk) > func(zk):
        if (k == 3):
            zkp1 = ak + (3 - math.sqrt(5)) / 2 * (bk - ak)
            akp1 = yk
            bkp1 = bk
            ykp1 = zk
        else:
            akp1 = yk
            bkp1 = bk
            ykp1 = zk
            zkp1 = akp1 + bkp1 - zk
    ak = akp1
    bk = bkp1
    yk = ykp1
    zk = zkp1
    delta = abs(akp1 - bkp1)
print('k = ', k, 'ak = ', ak, 'bk = ', bk, 'x* = ', (akp1 + bkp1)/2)
