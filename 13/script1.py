busesLine = []
timestamp = 0
minTime = 99999
finalBus = 0

with open('input.txt') as file:
    data = file.read().split('\n')
    timestamp = int(data[0])
    busesLine = list(data[1])
    for line in data:
        busesLine = line.split(',')

for bus in busesLine:
    if bus != 'x':
        bus = int(bus)
        busId = bus
        while (busId < timestamp):
            busId += bus
        if busId % timestamp < minTime:
            minTime = busId % timestamp
            finalBus = bus

print(finalBus * minTime)