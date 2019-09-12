from math import sqrt

P = lambda x: x*(3*x - 1)/2

def is_pent(n):
    if ((sqrt(1 + 24*n) + 1)/6)%1 == 0:
        return True
    else:
        return False

for a in range(1, 10000):
    for b in range(a, 10000):
        c = P(a)+P(b)
        if is_pent(c):
            if is_pent(P(b) + c):
                print(P(a))
            if is_pent(P(a) + c):
                print(P(b))
