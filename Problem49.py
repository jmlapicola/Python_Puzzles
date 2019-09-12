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

def perm(string):
    length = len(string)
    if length == 2:
        return [string, string[1] + string[0]]
    else:
        permutations = list()
        for n, digit in enumerate(string):
            subs = perm(string[0:n] + string[n+1:])
            for sub in subs:
                permutations.append(digit + sub)
        return permutations

for n1 in range(1000, 10000):
    if isPrime(n1):
        permutations = perm(str(n1))
        for permutation in permutations:
            n2 = int(permutation)
            dif = n2 - n1
            if dif >= 1 and isPrime(n2):
                n3 = n2 + dif
                if str(n3) in permutations and isPrime(n3):
                    print(n1, n2, n3)
