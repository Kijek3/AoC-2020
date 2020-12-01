numbers = []

with open('input.txt') as file:
    data = file.read().split()
    for line in data:
        numbers.append(int(line))

for i in range(0, len(numbers)):
    for j in range(i, len(numbers)):
        if numbers[i] + numbers[j] == 2020:
            print(numbers[i], numbers[j], numbers[i] * numbers[j])