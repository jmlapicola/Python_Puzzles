def tri(n):
    return n*(n+1)//2

def squ(n):
    return n**2

def pent(n):
    return n*(3*n-1)//2

def hex(n):
    return n*(2*n-1)

def hept(n):
    return n*(5*n-3)//2

def oct(n):
    return n*(3*n-2)

def poly(shape, n):
    if shape == 3:
        return tri(n)
    elif shape == 4:
        return squ(n)
    elif shape == 5:
        return pent(n)
    elif shape == 6:
        return hex(n)
    elif shape == 7:
        return hept(n)
    elif shape == 8:
        return oct(n)
    else:
        return 0

def nextPoly(first, last, left):
    if len(left) == 1:
        shape = left[0]
        n = start[shape]
        a_n = poly(shape, i)
        while a_n < 10000:
            string = str(a_n)
            if string[:2] == last and string[2:] == first:
                print(a_n, shape)
                return a_n
            else:
                n += 1
                a_n = poly(shape, n)
        return 0
    else:
        for shape in left:
            n = start[shape]
            a_n = poly(shape, i)
            while a_n < 10000:
                string = str(a_n)
                if string[:2] == last:
                    remainder = left[:]
                    remainder.remove(shape)
                    sum = nextPoly(first, string[2:], remainder)
                    if sum > 0:
                        print(a_n, shape, a_n + sum)
                        return a_n + sum
                n += 1
                a_n = poly(shape, n)
    return 0


start = [0,0,0,45,32,26,23,21,19]

left = [7,6,5,4,3]

i = start[8]
a_n = oct(i)
while a_n < 10000:
    number = str(a_n)
    sum = nextPoly(number[:2], number[2:], left)
    if sum:
        print(a_n, a_n + sum)
    i+=1
    a_n = oct(i)
