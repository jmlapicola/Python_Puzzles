def listPrimes(n):
    composites = {2}
    primes = list()
    for i in range(3, n + 1, 2):
        if i not in composites:
            primes.append(i)
            composites = composites.union(set(range(2*i, n + 1, i)))
    return primes

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

primes = listPrimes(100000)
maxLen = 0
maxSum = 0
start = 0
startsum = 0
while startsum < 1000000:
    length = maxLen
    startsum = sum(primes[start:start + length])
    total = startsum
    while total < 1000000:
        if isPrime(total):
            maxSum = total
            maxLen = length
            print(length, total)
        length += 1
        total = sum(primes[start:start + length])
    start += 1
print(maxSum)
