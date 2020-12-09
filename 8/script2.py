instructions = []
instructionsCopy = []
indexes = []
lastIndex = 0

with open('input.txt') as file:
    data = file.read().split('\n')
    for line in data:
        instructions.append(line.split())

j = 0
founded = False
while (not founded):
    instructionsCopy = []
    for i in range(0, len(instructions)):
        instructionsCopy.append(instructions[i].copy())
    accumulator = 0
    i = 0
    indexes = []

    for j in range(lastIndex + 1, len(instructionsCopy)):
        if instructionsCopy[j][0] == "jmp":
            instructionsCopy[j][0] = "nop"
            lastIndex = j
            break
        elif instructionsCopy[j][0] == "nop":
            instructionsCopy[j][0] = "jmp"
            lastIndex = j
            break

    while(i not in indexes):
        indexes.append(i)
        if instructionsCopy[i][0] == "acc":
            accumulator += int(instructionsCopy[i][1])
            i += 1
        elif instructionsCopy[i][0] == "jmp":
            i += int(instructionsCopy[i][1])
        elif instructionsCopy[i][0] == "nop":
            i += 1
        if i >= len(instructionsCopy):
            founded = True
            break

print(accumulator)