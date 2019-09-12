from math import sqrt

H = lambda x: x*(2*x-1)

def is_tri(n):
    if ((sqrt(1 + 8*n) + 1)/2)%1 == 0:
        return True
    else:
        return False

def is_pent(n):
    if ((sqrt(1 + 24*n) + 1)/6)%1 == 0:
        return True
    else:
        return False

max = 40755
n = 143
while max <= 40755:
    Hn = H(n)
    if is_tri(Hn) and is_pent(Hn):
        max = Hn
        print(Hn)
    n += 1
