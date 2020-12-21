ranges = []
rangesSet = []
tickets = []
inputWay = 0
result = 0

with open('input.txt') as file:
    data = file.read().split('\n')
    for line in data:
        if line == '':
            inputWay += 1
            continue
        if inputWay == 0:
            line = line.split(" or ")
            line[0] = line[0].split(": ")[1]
            ranges.append(line)
        if inputWay == 2:
            line = line.split(",")
            tickets.append(line)

for i in range(len(ranges)):
    for j in range(len(ranges[i])):
        actualRange = ranges[i][j].split("-")
        actualRange[0] = int(actualRange[0])
        actualRange[1] = int(actualRange[1])
        for number in range(actualRange[0], actualRange[1] + 1):
            rangesSet.append(number)

rangesSet = set(rangesSet)
for ticket in tickets:
    for value in ticket:
        if int(value) not in rangesSet:
            result += int(value)

print(result)