numbers = []
offset = 0

with open('input.txt') as file:
    data = file.read().split('\n')
    for line in data:
        numbers.append(int(line))

for i in range(25, len(numbers)):
    founded = False
    for j in range(offset, 25 + offset):
        for k in range(j + 1, 25 + offset):
            if numbers[j] + numbers[k] == numbers[25 + offset]:
                founded = True
                break
    if not founded:
        print(numbers[i])
        break
    offset += 1