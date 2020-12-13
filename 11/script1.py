grid = []
newGrid = []
changed = True

with open('input.txt') as file:
    data = file.read().split('\n')
    for line in data:
        newGrid.append(list(line))

def checkSeat(startY, startX, changeY, changeX):
    actualX = startX + changeX
    actualY = startY + changeY
    if actualX >= 0 and actualX < len(grid[startY]) and actualY >= 0 and actualY < len(grid):
        if grid[actualY][actualX] == '#':
            return 1
    return 0

while (changed):
    changed = False
    grid = list(map(list, newGrid))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != '.':
                occupiedNumber = 0
                occupiedNumber += checkSeat(i, j, -1, -1)
                occupiedNumber += checkSeat(i, j, -1, 0)
                occupiedNumber += checkSeat(i, j, -1, 1)
                occupiedNumber += checkSeat(i, j, 0, -1)
                occupiedNumber += checkSeat(i, j, 0, 1)
                occupiedNumber += checkSeat(i, j, 1, -1)
                occupiedNumber += checkSeat(i, j, 1, 0)
                occupiedNumber += checkSeat(i, j, 1, 1)

                if grid[i][j] == 'L' and occupiedNumber == 0:
                    newGrid[i][j] = '#'
                    changed = True
                elif grid[i][j] == '#' and occupiedNumber >= 4:
                    newGrid[i][j] = 'L'
                    changed = True

print(sum([i.count('#') for i in newGrid]))