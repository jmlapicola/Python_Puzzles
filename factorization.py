def factors(n):
    rem = n
    i = 2
    fac = list()
    while i**2 <= rem:
        if rem % i == 0:
            fac.append(i)
            rem //= i
        else:
            i += 1
    fac.append(rem)
    return fac
