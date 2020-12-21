rangesSet = []
tickets = []
validTickets = []
valids = [[]] * 20
rules = {}
inputWay = 0
result = 0

with open('input.txt') as file:
    data = file.read().split('\n')
    for line in data:
        if line == '':
            inputWay += 1
            continue
        if inputWay == 0:
            line = line.split(": ")
            line[1] = line[1].split(" or ")
            rules[line[0]] = line[1]
        if inputWay == 2:
            line = line.split(",")
            tickets.append(line)
# print(rules)
for key in rules:
    for j in range(2):
        actualRange = rules[key][j].split("-")
        actualRange[0] = int(actualRange[0])
        actualRange[1] = int(actualRange[1])
        for number in range(actualRange[0], actualRange[1] + 1):
            rangesSet.append(number)

rangesSet = set(rangesSet)
# print(rangesSet)
for ticket in tickets:
    validTicket = True
    for value in ticket:
        if int(value) not in rangesSet:
            validTicket = False
    if validTicket:
        validTickets.append(ticket)

i = 0
columnCounters = [0] * 20
for key in rules:
    actualRange1 = rules[key][0].split("-")
    actualRange1[0] = int(actualRange1[0])
    actualRange1[1] = int(actualRange1[1])
    actualRange2 = rules[key][1].split("-")
    actualRange2[0] = int(actualRange2[0])
    actualRange2[1] = int(actualRange2[1])
    valids[i] = []
    for k in range(0, 20):
        isValid = 1
        for ticket in validTickets:
            if int(ticket[k]) not in range(actualRange1[0], actualRange1[1] + 1) and int(ticket[k]) not in range(actualRange2[0], actualRange2[1] + 1):
                isValid = 0
        valids[i].append(isValid)
        columnCounters[k] += isValid
    print(valids[i], i)
    i += 1
print(columnCounters)