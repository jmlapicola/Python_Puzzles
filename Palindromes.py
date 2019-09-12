def isPalindrome(x):
    string = str(x)
    length = len(string)
    n = 0
    while n < (length/2):
        if string[n] != string[-1-n]:
            return False
        n = n + 1
    return True

i1 = 999
i2 = i1
largest = 0
while i1>0:
    while i2 >= i1:
        if isPalindrome(i1*i2) and i1*i2 > largest:
            largest = i1*i2
            print(i1)
            print(i2)
            print(largest)
        i2 = i2 - 1
    i2 = 999
    i1 = i1 - 1
