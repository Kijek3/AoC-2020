numbers = []

with open('input.txt') as file:
    data = file.read().split('\n')
    for line in data:
        numbers.append(int(line))

maxNumber = max(numbers)
actualNumber = 0
diff = 0
diffs = []
countOne = 0
countThree = 0
while (actualNumber < maxNumber):
    diff = 0
    while (True):
        actualNumber += 1
        diff += 1
        if actualNumber in numbers:
            diffs.append(diff)
            if diff == 1:
                countOne += 1
            else:
                countThree += 1
            break
print(countOne * (countThree + 1))