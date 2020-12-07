mapTab = []

with open('input.txt') as file:
    data = file.read().split('\n')
    for line in data:
        mapTab.append(list(line))

def checkSlope(xChange, yChange):
    x = 0
    y = 0
    counter = 0
    while True:
        if mapTab[y][x] == '#':
            counter += 1
        if y == 322:
            break
        x = (x + xChange) % 31
        y += yChange
    return counter

print(checkSlope(3,1)) #Part 1
print(checkSlope(1,1) * checkSlope(3,1) * checkSlope(5,1) * checkSlope(7,1) * checkSlope(1,2)) #Part 2