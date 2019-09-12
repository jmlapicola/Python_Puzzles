n = 10
total = 0
while True: #nasty but effective
    sum = 0
    for digit in str(n):
        sum += int(digit)**5
    if sum == n:
        total += n
        print(n, total)
    n += 1
