def paths(x,y):
    if x == 0:
        return 1
    elif x == 1:
        return (y + 1)
    elif x == 2:
        return (y+1)*(y+2)//2
    elif x == y:
        return 2*paths(x-1, y)
    elif x > y:
        return paths(y, x)
    else:
        return paths(y-1,x) + paths(y, x-1)

print(paths(20,20))
