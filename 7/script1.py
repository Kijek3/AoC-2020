rules = []
colors = ["shiny gold"]
counter = 0
changed = True

with open('input.txt') as file:
    data = file.read().split('\n')
    for line in data:
        rules.append(line.split())

while(changed):
    changed = False
    for rule in rules:
        for color in colors:
            for i in range(5, len(rule)):
                if rule[i] == color.split()[0] and rule[i+1] == color.split()[1]:
                    counter += 1
                    if rule[0] + " " + rule[1] not in colors:
                        colors.append(rule[0] + " " + rule[1])
                        changed = True

print(len(colors))