instructions = []
indexes = []
accumulator = 0
i = 0

with open('input.txt') as file:
    data = file.read().split('\n')
    for line in data:
        instructions.append(line.split())

while(i not in indexes):
    indexes.append(i)
    if instructions[i][0] == "acc":
        accumulator += int(instructions[i][1])
        i += 1
    elif instructions[i][0] == "jmp":
        i += int(instructions[i][1])
    elif instructions[i][0] == "nop":
        i += 1

print(accumulator)