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
        address = bin(int(bitmask[0]))[2:]
        addresses = []
        addressStr = ''
        changedX = False
        for i in range(len(mask)):
            if mask[len(mask) - 1 - i] == 'X':
                addressStr = 'X' + addressStr
            elif mask[len(mask) - 1 - i] == '1':
                addressStr = '1' + addressStr
            elif mask[len(mask) - 1 - i] == '0':
                if len(address) - 1 - i < 0:
                    addressStr = '0' + addressStr
                else:
                    addressStr = address[len(address) - 1 - i] + addressStr
        addresses.append(addressStr)
        i = 0
        while i < len(addresses):
            addressCopy = list(addresses[i])
            addressStr = ''
            if 'X' in addressCopy:
                xIndex = addressCopy.index('X')
                addresses.remove(addresses[i])
                addressCopy[xIndex] = '0'
                addresses.append("".join(addressCopy))
                addressCopy[xIndex] = '1'
                addresses.append("".join(addressCopy))
            else:
                i += 1
        value = int(bitmask[1])
        # Slow method
        for item in addresses:
            addConv = int(item, 2)
            if addConv in usedMemory:
                memory[usedMemory.index(addConv)][1] = value
            else:
                usedMemory.append(addConv)
                memory.append([addConv, value])

print(sum(n for _, n in memory))