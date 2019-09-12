def paths(x,y):
    if x == 1:
        return (y + 1)
    else:
        routes = 1
        for p in range(y):
            routes += paths(x-1, p+1)
        return routes

print(paths(15,15))
