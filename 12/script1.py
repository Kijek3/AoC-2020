directions = []
facing = 1
faces = ['N', 'E', 'S', 'W']
x = 0
y = 0

with open('input.txt') as file:
    data = file.read().split('\n')
    for line in data:
        directions.append(line)

for direction in directions:
    number = int(direction[1:])
    if direction[0] == 'N':
        y += number
    elif direction[0] == 'S':
        y -= number
    elif direction[0] == 'E':
        x += number
    elif direction[0] == 'W':
        x -= number
    elif direction[0] == 'L':
        facing -= number // 90
        facing %= 4
    elif direction[0] == 'R':
        facing += number // 90
        facing %= 4
    elif direction[0] == 'F':
        if faces[facing] == 'N':
            y += number
        if faces[facing] == 'S':
            y -= number
        if faces[facing] == 'E':
            x += number
        if faces[facing] == 'W':
            x -= number

print(abs(x) + abs(y))
    