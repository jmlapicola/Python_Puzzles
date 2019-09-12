def trunc(n):
    number = str(n)
    length = len(number)
    numbers = {int(number)}
    for i in range(1, length):
        numbers.add(int(number[i:]))
        numbers.add(int(number[:i]))
    return numbers

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    max = n**(1/2)
    i = 3
    while i <= max:
        if n % i == 0:
            return False
        i = i + 2
    return True

def truncPrime(n):
    for i in trunc(n):
        if not isPrime(i):
            return False
    return True

sum = 0
for i in range(10, 1000000):
    if truncPrime(i):
        sum += i
        print(i)
print(sum)
