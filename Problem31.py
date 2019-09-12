ways = 1
for p100 in range(3):
    for p50 in range(5):
        for p20 in range(11):
            for p10 in range(21):
                for p5 in range(41):
                    for p2 in range(101):
                        total = p100*100 + p50*50 + p20*20 + p10*10 + p5*5 + p2*2
                        if total <= 200:
                            ways +=1
print(ways)
