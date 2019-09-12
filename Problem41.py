def isPandigital(n):
    string = str(n)
    length = len(string)
    should = {str(n) for n in range(1, length + 1)}
    digits = set()
    for n in string:
        if n in digits:
            return False
        else:
            digits.add(n)
    if digits == should:
        return True
    else:
        return False

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

pandigitals = list()
largest_pan = '987654321'
for n in range(len(largest_pan)):
    pandigitals += perm(largest_pan[n:])

for num in pandigitals:
    if isPrime(int(num)):
        print(num)
        break
