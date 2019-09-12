def cycle_length(num):
    place = 0
    remainder = 1
    history = list()
    while remainder not in history:
        history.append(remainder)
        remainder = remainder % num
        if remainder == 0:
            return 0
        remainder *= 10
        place += 1
    return place - history.index(remainder)

maxlen = 0
maxi = 0
for i in range(1,1000):
    length = cycle_length(i)
    if length > maxlen:
        maxlen = length
        maxi = i
        print(maxlen, maxi)
