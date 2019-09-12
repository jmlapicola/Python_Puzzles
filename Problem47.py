def factors(n):
    rem = n
    i = 2
    fac = set()
    while i**2 <= rem:
        if rem % i == 0:
            fac.add(i)
            rem //= i
        else:
            i += 1
    fac.add(rem)
    return len(fac)

consecutive = 0
i = 1
while consecutive < 4:
    if factors(i) == 4:
        consecutive += 1
    else:
        consecutive = 0
    i += 1

print(i - 4)
