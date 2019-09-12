from math import sqrt

def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n%2 == 0 or n%3 == 0 or n < 2:
        return False
    max = n**(1/2)
    i = 5
    while i <= max:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def CGconj(n):
    for i in range(2, n):
        if isPrime(i):
            if sqrt((n - i)/2) % 1 == 0:
                return True
    return False

CG = True
i = 9
while CG:
    if not isPrime(i):
        if not CGconj(i):
            CG = False
            break
    i += 2
print(i)
