def collatz(n):
    l = 1
    while n > 1:
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        l += 1
    return l

longest = 0
start = 0
for i in range(1000000):
    if collatz(i) > longest:
        longest = collatz(i)
        start = i
    print(i)
print(start)
