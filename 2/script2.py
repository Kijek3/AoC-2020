policy = []
counter = 0

with open('input.txt') as file:
    data = file.read().split('\n')
    for line in data:
        policy.append(line)

for police in policy:
    req = police.split()
    range1 = int(req[0].split('-')[0])
    range2 = int(req[0].split('-')[1])
    letterP = req[1][0]
    password = req[2]
    goodLetters = 0
    if password[range1 - 1] == letterP:
        goodLetters += 1
    if password[range2 - 1] == letterP:
        goodLetters += 1
    if goodLetters == 1:
        counter += 1

print(counter)