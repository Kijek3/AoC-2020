counter = 0
answersList = []

with open('input.txt') as file:
    data = file.read().split('\n\n')
    for line in data:
        line = line.split()
        answersSets = []
        for answer in line:
            answersSets.append(set(answer))
        answersList.append(answersSets)

for answers in answersList:
    counter += len(set.intersection(*answers))

print(counter)