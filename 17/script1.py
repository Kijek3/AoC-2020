sector = []

with open('input.txt') as file:
    data = file.read().split('\n')
    for line in data:
        sector.append(line)

cubes = set()
for y in range(len(sector)):
    for x in range(len(sector[y])):
        if sector[y][x] == "#":
            cubes.add((x, y, 0))

def neighbors(x, y, z):
    for nx in range(x - 1, x + 2):
        for ny in range(y - 1, y + 2):
            for nz in range(z - 1, z + 2):
                if nx == x and ny == y and nz == z:
                    continue
                yield (nx, ny, nz)

for _ in range(6):
    cubesAfter = set()
    allX = [t[0] for t in cubes]
    allY = [t[1] for t in cubes]
    allZ = [t[2] for t in cubes]
    for x in range(min(allX) - 1, max(allX) + 2):
        for y in range(min(allY) - 1, max(allY) + 2):
            for z in range(min(allZ) - 1, max(allZ) + 2):
                counter = 0
                for n in neighbors(x, y, z):
                    if n in cubes:
                        counter += 1
                if (x, y, z) in cubes and (counter == 2 or counter == 3):
                    cubesAfter.add((x, y, z))
                elif counter == 3:
                    cubesAfter.add((x, y, z))
    cubes = cubesAfter

print(len(cubes))