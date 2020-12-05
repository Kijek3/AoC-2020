import math
seats = []

with open('input.txt') as file:
    data = file.read().split()
    for line in data:
        seats.append(line)

maxId = 0

for i in range(0, len(seats)):
    minY = minX = 0
    maxY = 127
    maxX = 7
    for letter in seats[i]:
        if letter == 'F':
            maxY = math.floor((minY + maxY) / 2)
        elif letter == 'B':
            minY = math.ceil((minY + maxY) / 2)
        elif letter == 'R':
            minX = math.ceil((minX + maxX) / 2)
        elif letter == 'L':
            maxX = math.floor((minX + maxX) / 2)
    if maxY * 8 + maxX > maxId:
        maxId = maxY * 8 + maxX
print(maxId)