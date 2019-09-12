def isPandigital(n1, n2):
    digits = set()
    for n in str(n1):
        if n in digits:
            return False
        else:
            digits.add(n)
    for n in str(n2):
        if n in digits:
            return False
        else:
            digits.add(n)
    for n in str(n1*n2):
        if n in digits:
            return False
        else:
            digits.add(n)
    if len(digits) == 9 and '0' not in digits:
        return True
    else:
        return False

ways = set()
for n1 in range(2, 10000):
    n2 = 2
    while n1*n2 < 100000:
        if isPandigital(n1, n2):
            print(n1, n2, n1*n2)
            ways.add(n1*n2)
        n2 +=1
print(sum(ways))
