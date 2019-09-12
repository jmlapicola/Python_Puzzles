def circles(n):
    number = str(n)
    length = len(number)
    circles = set()
    for i in range(length):
        circles.add(int(number[i:] + number[:i]))
    return circles

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

def circPrime(n):
    for i in circles(n):
        if not isPrime(i):
            return False
    return True

count = 0
for i in range(2,1000000):
    if circPrime(i):
        count += 1
        print(i)
print(count)
