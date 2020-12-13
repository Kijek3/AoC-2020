directions = []
shipX = 0
shipY = 0
waypX = 10
waypY = 1

with open('input.txt') as file:
    data = file.read().split('\n')
    for line in data:
        directions.append(line)

for direction in directions:
    number = int(direction[1:])
    if direction[0] == 'N':
        waypY += number
    elif direction[0] == 'S':
        waypY -= number
    elif direction[0] == 'E':
        waypX += number
    elif direction[0] == 'W':
        waypX -= number
    elif direction[0] == 'L':
        for i in range(number // 90):
            waypX, waypY = -waypY, waypX
    elif direction[0] == 'R':
        for i in range(number // 90):
            waypX, waypY = waypY, -waypX
    elif direction[0] == 'F':
        shipX += waypX * number
        shipY += waypY * number

print(abs(shipX) + abs(shipY))
    