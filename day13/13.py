f = open('input.txt', 'r')
input = f.read().split('\n\n')
grids=[]
for line in input:
    grids.append(line.split('\n'))

def transformColGrid(grid):
    lenRows = len(grid)
    lenColumns = len(grid[0])
    columns = [[] for _ in range(lenColumns)]
    for col in range(lenColumns):
        for row in range(lenRows):
            columns[col].append(grid[row][col])
    return columns

def getReflectionNum(grid):
    for column in range(1, len(grid[0])):
        spit = min(column, len(grid[0])-column)
        reflection = True
        for line in grid:
            if line[column-spit:column] != line[column:column+spit][::-1]:
                reflection = False
                break
        if reflection:
            return column


verticals = 0
horizontals = 0
for grid in grids:
  rows = [[x for x in row] for row in grid]
  columns = transformColGrid(grid)
  vertical = getReflectionNum(columns)
  horizontal = getReflectionNum(rows)
  if(horizontal):
      horizontals += horizontal 
  if(vertical):
      verticals += vertical * 100

print(verticals+horizontals)


