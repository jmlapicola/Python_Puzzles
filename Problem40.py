string = ""
i = 1
while len(string) <= 1000001:
    string += str(i)
    i += 1

d = int(string[0])
d *= int(string[9])
d *= int(string[99])
d *= int(string[999])
d *= int(string[9999])
d *= int(string[99999])
d *= int(string[999999])

print(d)
