# Use intersection instead
counter = 0

with open('input.txt') as file:
    data = file.read().split('\n\n')
    for line in data:
        line = line.split()
        if len(line) == 1:
            counter += len(set(line[0]))
        elif len(line) > 1:
            for letter in line[0]:
                valid = True
                if valid:
                    for i in range(1, len(line)):
                        if letter not in line[i]:
                            valid = False
                            break
                if valid:
                    counter += 1
print(counter)