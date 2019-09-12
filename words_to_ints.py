from math import sqrt

def is_tri(n):
    if ((sqrt(1 + 8*n) + 1)/2)%1 == 0:
        return True
    else:
        return False

file = open("words.txt")
names = file.read()
file.close()
names = names.replace('"','')
list = names.split(",")
list.sort()

total = 0
for i, name in enumerate(list):
    score = 0
    for char in name:
        score += ord(char) - 64
    if is_tri(score):
        total += 1
print(total)
