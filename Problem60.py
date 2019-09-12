# n = 100,000 takes 1 min, n = 1,000,000 takes 1 hour
def listPrimes(n):
    composites = set()
    primes = list()
    for i in range(2, n + 1):
        if i not in composites:
            primes.append(i)
            composites = composites.union(set(range(2*i, n + 1, i)))
    return primes

def listConcat2(l1):
    n = len(l1)
    pairs = []
    for s1 in l1:
        l2 = list(l1)
        l2.remove(s1)
        for s2 in l2:
            s3 = str(s1) + str(s2)
            pairs.append(int(s3))
    return pairs

print("ListingPrimes...")
plist = listPrimes(100000)
print("DONE")

def isPrime(n):
    if n in plist:
        return True
    elif n <= 100000:
        return False
    else:
        max = n**(1/2)
        for p in plist:
            if n%p == 0:
                return False
            elif p > max:
                return True
        i = 100001
        while i <= max:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
'''
testlist = listConcat2([3,7,109,673,677])
print(testlist)
for n in testlist:
    if not isPrime(n):
        print(n)
'''
primes = list(plist)

primes.remove(2)
primes.remove(5)

minsum = 50000

i1 = 0
p1 = primes[i1]
sum1 = p1
while sum1 + 4*p1 < minsum:
    print(p1)
    i2 = i1 + 1
    p2 = primes[i2]
    sum2 = sum1 + p2
    while sum2 + 3*p2 < minsum:
        pairs2 = listConcat2([p1,p2])
        success2 = True
        for n in pairs2:
            if not isPrime(n):
                success2 = False
                break
        if success2:
            print(p1,p2)
            i3 = i2 + 1
            p3 = primes[i3]
            sum3 = sum2 + p3
            while sum3 + 2*p3 < minsum:
                pairs3 = listConcat2([p1,p2,p3])
                success3 = True
                for n in pairs3:
                    if not isPrime(n):
                        success3 = False
                        break
                if success3:
                    print(p1,p2,p3)
                    i4 = i3 + 1
                    p4 = primes[i4]
                    sum4 = sum3 + p4
                    while sum4 + p4 < minsum:
                        pairs4 = listConcat2([p1,p2,p3,p4])
                        success4 = True
                        for n in pairs4:
                            if not isPrime(n):
                                success4 = False
                                break
                        if success4:
                            print(p1,p2,p3,p4)
                            i5 = i4 + 1
                            p5 = primes[i5]
                            sum5 = sum4 + p5
                            while sum5 < minsum:
                                pairs5 = listConcat2([p1,p2,p3,p4,p5])
                                success5 = True
                                for n in pairs5:
                                    if not isPrime(n):
                                        success5 = False
                                        break
                                if success5:
                                    minsum = sum5
                                    print(p1,p2,p3,p4,p5," => ",sum5)
                                i5 +=1
                                p5 = primes[i5]
                                sum5 = p5 + sum4
                        i4 +=1
                        p4 = primes[i4]
                        sum4 = p4 + sum3
                i3 +=1
                p3 = primes[i3]
                sum3 = p3 + sum2
        i2 +=1
        p2 = primes[i2]
        sum2 = p2 + sum1
    i1 +=1
    p1 = primes[i1]
    sum1 = p1

print(minsum)
