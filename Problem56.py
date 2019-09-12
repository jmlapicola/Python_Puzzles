def sumdig(n):
    digits = str(n)
    sum = 0
    for digit in digits:
        sum += int(digit)
    return sum

max = 0

for a in range(100):
    for b in range(100):
        sum = sumdig(a**b)
        if sum > max:
            max = sum
print(max)
