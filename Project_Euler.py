f = open("input.txt")
input = f.read()
f.close()
a = [0] * 20
for i in range(20):
    a[i] = [0] * 20
    for j in range(20):
        p = i*3 + j*60
        a[i][j] = int(input[p:p+2])
max = 0
for i in range(20):
    for j in range(17):
        product = a[i][j]*a[i][j+1]*a[i][j+2]*a[i][j+3]
        if product > max:
            max = product
for i in range(17):
    for j in range(20):
        product = a[i][j]*a[i+1][j]*a[i+2][j]*a[i+3][j]
        if product > max:
            max = product
for i in range(17):
    for j in range(17):
        product = a[i][j]*a[i+1][j+1]*a[i+2][j+2]*a[i+3][j+3]
        if product > max:
            max = product
for i in range(17):
    for j in range(17):
        product = a[i][j+3]*a[i+1][j+2]*a[i+2][j+1]*a[i+3][j]
        if product > max:
            max = product
print(max)
