def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    max = n**(1/2)
    i = 3
    while i <= max:
        if n % i == 0:
            return False
        i = i + 2
    return True

maxn = 0
maxa = 0
maxb = 0
for b in range(1000):
    if isPrime(b):
        for a in range(-1000, 1000):
            n = 0
            while isPrime(n**2 + a*n + b):
                n += 1
            if n > maxn:
                maxn = n
                maxa = a
                maxb = b
print(maxn, maxa, maxb, maxa*maxb)
