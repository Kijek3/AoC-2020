questions = []

with open('input.txt') as file:
    data = file.read().split('\n\n')
    for line in data:
        questions.append(set(line.replace('\n','')))

counter = 0

for question in questions:
    counter += len(question)

print(counter)