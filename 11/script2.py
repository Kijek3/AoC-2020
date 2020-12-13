grid = []
newGrid = []
changed = True

with open('input.txt') as file:
    data = file.read().split('\n')
    for line in data:
        newGrid.append(list(line))

def checkSeats(startY, startX, changeY, changeX):
    seatFounded = False
    result = 0
    actualX = startX + changeX
    actualY = startY + changeY
    if actualX < 0 or actualX >= len(grid[startY]) or actualY < 0 or actualY >= len(grid):
            seatFounded = True
    while (not seatFounded):
        if grid[actualY][actualX] == '#':
            result = 1
            seatFounded = True
        elif grid[actualY][actualX] == 'L':
            seatFounded = True
        actualX += changeX
        actualY += changeY
        if actualX < 0 or actualX >= len(grid[startY]) or actualY < 0 or actualY >= len(grid):
            seatFounded = True
    return result

while (changed):
    changed = False
    grid = list(map(list, newGrid))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != '.':
                occupiedNumber = 0
                occupiedNumber += checkSeats(i, j, -1, -1)
                occupiedNumber += checkSeats(i, j, -1, 0)
                occupiedNumber += checkSeats(i, j, -1, 1)
                occupiedNumber += checkSeats(i, j, 0, -1)
                occupiedNumber += checkSeats(i, j, 0, 1)
                occupiedNumber += checkSeats(i, j, 1, -1)
                occupiedNumber += checkSeats(i, j, 1, 0)
                occupiedNumber += checkSeats(i, j, 1, 1)

                if grid[i][j] == 'L' and occupiedNumber == 0:
                    newGrid[i][j] = '#'
                    changed = True
                elif grid[i][j] == '#' and occupiedNumber >= 5:
                    newGrid[i][j] = 'L'
                    changed = True

print(sum([i.count('#') for i in newGrid]))