from bisect import bisect_left
numbers = []

with open('input.txt') as file:
    data = file.read().split('\n')
    for line in data:
        numbers.append(int(line))

numbers.sort()
numbers.append(max(numbers) + 3)

options = [0] * len(numbers) # Create array that contains zeros
for i in range(0, len(numbers)):
    if numbers[i] <= 3: # For numbers 1 - 3 don't make bisect
        options[i] = 2 * i
        continue
    ind = bisect_left(numbers, numbers[i] - 3) # Return number equal or lower (because we have sorted array)
    options[i] = sum(options[ind:i])
    
print(max(options))