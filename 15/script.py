def solution(amount):
    numbers = {}
    actualIndex = 2

    with open('input.txt') as file:
        data = file.read().split(',')
        for i, line in enumerate(data[:-1]):
            numbers[int(line)] = i + 1
            actualIndex += 1
        number = int(data[-1])

    while actualIndex <= amount:
        if number in numbers:
            nextNumber = actualIndex - numbers[number] - 1
            numbers[number] = actualIndex - 1
        else:
            nextNumber = 0
            numbers[number] = actualIndex - 1
        number = nextNumber
        actualIndex += 1
    
    return number

print(solution(2020)) # Part 1
print(solution(30000000)) # Part 2 (that takes around 10 seconds)