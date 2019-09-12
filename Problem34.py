from math import factorial

def dig_fact(n):
    digits = str(n)
    sum = 0
    for digit in digits:
        sum += factorial(int(digit))
    if sum == n:
        return True
    else:
        return False

i = 3
sum = 0
while True:
    if dig_fact(i):
        sum += i
        print(i, sum)
    i+=1
