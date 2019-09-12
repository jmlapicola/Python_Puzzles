f = open("input.txt")
lines = f.readlines()
f.close()
for n, line in enumerate(lines):
    lines[n] = [int(line[3*i:3*i+2]) for i in range(n + 1)]
for n in range(len(lines) - 2, -1, -1):
    for m in range(len(lines[n])):
        lines[n][m] = max(lines[n][m] + lines[n + 1][m], lines[n][m] + lines[n+1][m+1])
print(lines[0])
