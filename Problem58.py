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

ratio = 1
length = 0
n = 1
primes = 0
diagonals = 1

while ratio > .1:
    length +=2
    for side in range(4):
        n += length
        if isPrime(n):
            primes += 1
        diagonals +=1
    ratio = primes/diagonals
print(length + 1, ratio)
