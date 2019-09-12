num = 0
for power in range(100):
    base = 0
    while len(str(base**power)) <= power:
        if len(str(base**power)) == power:
            num += 1
            print(num, "-", base, "^", power, "=", base**power)
        base += 1
