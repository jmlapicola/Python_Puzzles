def simplifies(num, den):
    top = str(num)
    bot = str(den)
    if top[1] == bot[0] and bot[1] != '0':
        simple = int(top[0])/int(bot[1])
        if simple == num/den:
            return True

for a in range(11, 100):
    for b in range(11, a):
        if simplifies(b, a):
            print('{}/{}'.format(b, a))
