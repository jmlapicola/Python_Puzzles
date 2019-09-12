from math import factorial

digits = str(factorial(100))
sum = 0
for digit in digits:
    sum += int(digit)
print(sum)
