"""
AllenKll
12/8/2002 20:00

--- Day 8: Treetop Tree House ---

"""


file = open("input.txt", "r", encoding="ascii")  # , newline='\r\n')
line = "null"

grid = []

#read in whole grid
while line:
    line = file.readline()
    if not line:
        break
    line  = line.strip()

    row = list(line)
    grid.append(row)

numCols = len(grid[0])
numRows = len(grid)

bestScore = 0
#loop through all points INSIDE the outer square of trees, since the outer square is visible and we can just add it at the end.
for x in range(1,numCols-1):
    for y in range(1, numRows-1):
        treeHeight = grid[y][x]
        sceneicScore = 1
        # is visible from left?
        trees = 0
        for i in range(x-1, -1, -1):
            trees += 1
            if grid[y][i] >= treeHeight:
                break
        sceneicScore = sceneicScore * trees


        # is visible from right?
        trees = 0
        for i in range(x+1, numCols):
            trees += 1
            if grid[y][i] >=  treeHeight:
                break
        sceneicScore = sceneicScore * trees

        # is visible from down?
        trees = 0
        for i in range(y+1, numRows):
            trees += 1
            if grid[i][x] >=  treeHeight:
                break
        sceneicScore = sceneicScore * trees

        # is visible from up?
        trees = 0
        for i in range(y-1, -1, -1):
            trees += 1
            if grid[i][x] >=  treeHeight:
                vis = False
                break
        sceneicScore = sceneicScore * trees

        if sceneicScore > bestScore:
            bestScore = sceneicScore


print("Sceneic score=", bestScore)        
