def sum_divisors(n):
    sum  = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            sum += i
    return sum

def is_abundant(n):
    if sum_divisors(n) > n:
        return True
    else:
        return False

abundants = set()
for i in range(28111):
    if is_abundant(i):
        abundants.add(i)
#print(abundants)

def sum_of_abun(n):
    for num in abundants:
        if n - num in abundants:
            return True
    return False

sum = 0
for i in range(28123):
    if not sum_of_abun(i):
        sum += i
        print(i)
print(sum)
