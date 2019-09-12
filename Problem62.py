def isPerm(string1, string2):
    for c in string1:
        if c not in string2:
            return False
        else:
            toDelete = string2.find(c)
            string2 = string2[0:toDelete] + string2[toDelete + 1:]
    if len(string2) == 0:
        return True
    return False

cubes = []
perms = 1
n = 1
while perms < 5:
    n += 1
    print(n)
    perms = 1
    for int in cubes:
        if isPerm(int, str(n**3)):
            perms += 1
    cubes.append(str(n**3))

for int in cubes:
    if isPerm(int, str(n**3)):
        print(int)
