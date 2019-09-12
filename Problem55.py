def isPalindrome(x):
    string = str(x)
    length = len(string)
    n = 0
    while n < (length/2):
        if string[n] != string[-1-n]:
            return False
        n = n + 1
    return True

def isLychrel(n):
    sum = n
    for i in range(50):
        string = str(sum)
        sum += int(string[::-1])
        if isPalindrome(sum):
            return False
    return True

Lychrels = 0


for i in range(10000):
    if isLychrel(i):
        Lychrels += 1
        print(i)
print(Lychrels)
