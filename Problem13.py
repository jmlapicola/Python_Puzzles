f = open("input.txt")
ints = f.readlines()
f.close()
sum = 0
print(ints)
for n in ints:
    sum += int(n)
print(sum)
