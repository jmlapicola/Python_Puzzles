def paths(x,y):
    #creating matrix x by y
    grid = [0]*x
    for a in range(x):
        grid[a] = [0]*y
    #filling
    for a in range(x):
        grid[a][0] = a + 2
        b = 1
        while b < a:
            grid[a][b] = grid[a-1][b]+grid[a][b-1]
            b+=1
        if a > 0:
            grid[a][b] = 2*grid[a][b-1]
    return grid[x-1][y-1]

print(paths(20, 20))
