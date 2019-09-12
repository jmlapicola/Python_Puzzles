from math import sqrt

#determines primality
def isPrime(x):
    max = sqrt(x)
    i = 2
    while i <= max:
        if x%i == 0:
            return False
        i = i + 1
    return True

def isPrime2(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    max = sqrt(n)
    i = 3
    while i <= max:
        if n % i == 0:
            return False
        i = i + 2
    return True

def isPrime3(n):
    if n == 2 or n == 3:
        return True
    if n%2 == 0 or n%3 == 0 or n < 2:
        return False
    max = sqrt(n)
    i = 5
    while i <= max:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# n = 100,000 takes 1 min, n = 1,000,000 takes 1 hour
def listPrimes(n):
    composites = set()
    primes = list()
    for i in range(2, n + 1):
        if i not in composites:
            primes.append(i)
            composites = composites.union(set(range(2*i, n + 1, i)))
    return primes

plist = listPrimes(100000) #ceiling

def isPrimeFromList(n):
    if n in plist:
        return True
    elif n <= 100000: #ceiling
        return False
    else:
        max = sqrt(n)
        for p in plist:
            if n%p == 0:
                return False
            elif p > max:
                return True
        i = 100001 # (the first multiple of 6 after ceiling) - 1
        while i <= max:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
