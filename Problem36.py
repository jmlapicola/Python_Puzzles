def isPalindrome(x):
    string = str(x)
    length = len(string)
    n = 0
    while n < (length/2):
        if string[n] != string[-1-n]:
            return False
        n = n + 1
    return True

sum = 0
for n in range(1000000):
    if isPalindrome(n):
        binary = bin(n)
        if isPalindrome(binary[2:]):
            sum += n
            print(n, binary[2:])
print(sum)
