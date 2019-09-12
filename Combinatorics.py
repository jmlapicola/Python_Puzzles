import math

def numcomb(n, r):
    return math.factorial(n)/math.factorial(r)/math.factorial(n-r)

dvc = 0
for n in range(1,101):
    for r in range(1, n + 1):
        value = numcomb(n, r)
        if value > 1000000:
            dvc += 1
        print(n,'C', r, '=', value)

print(dvc)
