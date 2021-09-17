def minTotalDistance(grid):
    xcord=[]
    ycord=[]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c]==1:
                xcord.append(r)
    for c in range(len(grid[0])):
        for r in range(len(grid[0])):
            if grid[r][c]==1:
                ycord.append(c)
    x=xcord[int(len(xcord)/2)]
    y=ycord[int(len(ycord)/2)]
    dist=0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c]==1:
                dist+=abs(x-r)+abs(y-c)
    return dist