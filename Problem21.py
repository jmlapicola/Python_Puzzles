def sumOfFactors(n):
    sum  = 0
    for i in range(1, n//2 + 2):
        if n % i == 0:
            sum += i
    return sum

def isAmicable(n):
    if sumOfFactors(n) == n:
        return False
    elif sumOfFactors(sumOfFactors(n)) == n:
        return True
    else:
        return False

sum = 0
for n in range(10000):
    if isAmicable(n):
        sum += n
print(sum)
