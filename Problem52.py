def perm(string):
    length = len(string)
    if length == 2:
        return [string, string[1] + string[0]]
    else:
        permutations = list()
        for n, digit in enumerate(string):
            subs = perm(string[0:n] + string[n+1:])
            for sub in subs:
                permutations.append(digit + sub)
        return permutations

i = 1
j = 1

while j < 6:
    j = 1
    perms = perm(str(i))
    while True:
        if str(i*(j+1)) in perms:
            j += 1
        else:
            break
    print(i, j)
    i += 1
print(i)
