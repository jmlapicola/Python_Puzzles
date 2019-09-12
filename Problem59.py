file = open("cipher.txt")
message = file.read()
file.close()
letters = message.split(",")

numbers = []

for n in letters:
    numbers.append(int(n))

def isletter(n):
    if n < 65 or n > 122 or (n > 90 and n < 97):
        return False
    return True

def cypher(text, key):
    klength = len(key)
    vowels = 0
    mess = ''
    letters = 0
    spaces = 0
    for i, letter in enumerate(text):
        ktemp = i%klength
        newval = letter^key[ktemp]
        if (newval < 32 or newval > 124) and newval not in [9,10]:
            return None
        newchr = chr(newval)
        if newchr in 'AEIOUYaeiouy':
            vowels += 1
        if newchr == ' ':
            spaces += 1
        if isletter(newval):
            letters += 1
#        else:
#            if vowels == 0 and wordlen > 0:
#                return None
#            vowels = 0
#            wordlen = 0
        mess += newchr
    #if letters < (3*klength/4) or (spaces < klength/10):
    #    return None
    return mess

print(numbers)

k1 = 103
k2 = 111
k3 = 100
solution = cypher(numbers, [k1,k2,k3])

sum = 0
for n in solution:
    sum += ord(n)
print(sum)
