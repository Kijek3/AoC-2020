bitmasks = []
mask = '0' * 36
memory = []
usedMemory = []

with open('input.txt') as file:
    data = file.read().split('\n')
    for line in data:
        line = line.split(" = ")
        bitmasks.append(line)

for bitmask in bitmasks:
    if bitmask[0] == 'mask':
        mask = bitmask[1]
    else:
        value = bin(int(bitmask[1]))[2:]
        valueStr = ''
        for i in range(len(mask)):
            if mask[len(mask) - 1 - i] != 'X':
                valueStr = mask[len(mask) - 1 - i] + valueStr
            else:
                if len(value) - 1 - i < 0:
                    valueStr = '0' + valueStr
                else:
                    valueStr = value[len(value) - 1 - i] + valueStr
        if int(bitmask[0]) in usedMemory:
            memory[usedMemory.index(int(bitmask[0]))][1] = int(valueStr, 2)
        else:
            usedMemory.append(int(bitmask[0]))
            memory.append([int(bitmask[0]), int(valueStr, 2)])

print(sum(n for _, n in memory))