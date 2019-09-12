file = open("names.txt")
names = file.read()
file.close()
names = names.replace('"','')
list = names.split(",")
list.sort()
total_score = 0

for i, name in enumerate(list):
    score = 0
    for char in name:
        score += ord(char) - 64
    total_score += score*(i + 1)
print(total_score)
