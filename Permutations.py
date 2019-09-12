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
