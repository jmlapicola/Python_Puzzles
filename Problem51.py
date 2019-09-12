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

def powerSet(set0):
    if len(set0) == 1:
        return {frozenset(set0)}
    list0 = list(set0)
    subPowerSet = powerSet(set(list0[1:]))
    pSet = set(subPowerSet)
    for s in subPowerSet:
        unfrozenset = set(s)
        unfrozenset.add(list0[0])
        pSet.add(frozenset(unfrozenset))
        pSet.add(frozenset({list0[0]}))
    return pSet

i = 100000
notFound = True
while notFound:
    string = str(i)
    digitsReplaced = powerSet(set(range(len(string))))
    for digits in digitsReplaced:
        string = str(i)
        primes = 0
        for n in range(10):
            for digit in digits:
                string = string[:digit] + str(n) + string[(digit+1):]
            if isPrime(int(string)) and string[0] != '0':
                primes +=1
        if primes >=8:
            for digit in digits:
                string = string[:digit] + '*' + string[digit+1:]
            print(primes, string, "\nPRIMES")
            for n in range(10):
                for digit in digits:
                    string = string[:digit] + str(n) + string[(digit+1):]
                if isPrime(int(string)):
                    print(string)
            notFound = False
    i += 1
    print(i)
