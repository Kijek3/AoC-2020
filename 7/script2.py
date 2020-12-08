rules = {}

with open('input.txt') as file:
    data = file.read().split('\n')
    for line in data:
        line = line.split()
        key = line[0] + ' ' + line[1]
        values = []
        i = 4
        if line[i] != 'no':
            while(True):
                values.append((int(line[i]), line[i + 1] + ' ' + line[i + 2])) # Create quantity and color pair
                if '.' in line[i + 3]:
                    break
                i += 4
        rules[key] = values

def count_bags(quantity, color):
    if len(rules[color]) == 0:
        return quantity
    return quantity * (sum(count_bags(q, c) for q, c in rules[color]) + 1)

print(count_bags(1, "shiny gold") - 1)