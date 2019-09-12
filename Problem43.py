primes = [2, 3, 5, 7, 11, 13, 17]

def is_ssdiv(s):
    for i in range(7):
        if int(s[i+1:i+4]) % primes[i] != 0:
            return False
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

pandigitals = perm("9876543210")

primes = [2, 3, 5, 7, 11, 13, 17]

sum = 0
for num in pandigitals:
    if is_ssdiv(num):
        sum += int(num)
print(sum)
