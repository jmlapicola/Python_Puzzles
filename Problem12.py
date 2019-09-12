def divisors(x):
    divisors = 2
    for n in range(int(x**(1/2))):
        if tnum%(n+2) == 0:
            divisors += 2
    return divisors

i = 3
tnum = 3
while divisors(tnum) <= 500:
    tnum += i
    print(tnum)
    print(divisors(tnum))
    i+=1
print(tnum)
