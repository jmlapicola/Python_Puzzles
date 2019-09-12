num = 3
den = 2
count = 0

for i in range(1000):
    num2 = 2*den + num
    den = num + den
    num = num2
    if len(str(num)) > len(str(den)):
        count +=1
print(count)
