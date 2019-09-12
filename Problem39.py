from math import sqrt

def triangles(p):
    maxa = int(p/(sqrt(2) + 2)) + 1
    solutions = 0
    for a in range(1, maxa):
         remainder = (p**2 - 2*p*a) % (2*(p - a))
         #b = (p**2 - 2*p*a) / (2(p - a))
         if remainder == 0:
             solutions += 1
    return solutions

max_n = 0
max_p = 0

for p in range(1, 1001):
    n = triangles(p)
    if n > max_n:
        max_n = n
        max_p = p

print(max_p, max_n)
