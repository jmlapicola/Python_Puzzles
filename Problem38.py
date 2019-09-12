def isPandigital(string):
    digits = set()
    for n in string:
        if n in digits:
            return False
        else:
            digits.add(n)
    if len(digits) == 9 and '0' not in digits:
        return True
    else:
        return False

largest = 0
for num in range(1, 10000):
    n = 2
    string = str(num)
    while len(string) * n < 10:
        product = ''
        for i in range(1, n+1):
            product = product + str(i*num)
            if isPandigital(product):
                print(product)
                if int(product) > largest:
                    largest = int(product)
        n +=1
print(largest)
