def letters(n):
    if n == 1000:
        return 11
    else:
        sum = 0
        #digits
        one = n%10
        ten = (n//10)%10
        hundred = (n//100)%10
        #key
        ones = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
        tens = [0, 4, 6, 6, 5, 5, 5, 7, 6, 6]
        hundreds = [0, 10, 10, 12, 11, 11, 10, 12, 12, 11]
        #math
        sum = ones[one] + tens[ten] + hundreds[hundred]
        #accounting for "and"
        n0 = n%100
        if n > 100 and n0 != 0:
            sum += 3
        #excepetions (one letter):ten, eleven, twelve, thirteen, fifteen, eighteen
        if n0 == 10 or n0 == 11 or n0 == 12 or n0 == 13 or n0 == 15 or n0 == 18:
            sum -= 1
        return sum

total = 0
for i in range(1001):
    total += letters(i)
print(total)
