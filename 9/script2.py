numbers = []
offset = 0
searched = 0
numbersSum = []

with open('input.txt') as file:
    data = file.read().split('\n')
    for line in data:
        numbers.append(int(line))

for i in range(25, len(numbers)):
    founded = False
    for j in range(offset, 25 + offset):
        for k in range(j + 1, 25 + offset):
            if numbers[j] + numbers[k] == numbers[25 + offset]:
                founded = True
                break
    if not founded:
        searched = numbers[i]
        break
    offset += 1

# https://www.geeksforgeeks.org/find-subarray-with-given-sum/
def subArraySum(arr, n, sum): 
    for i in range(n): 
        curr_sum = arr[i]  
        j = i + 1
        while j <= n: 
            if curr_sum == sum:
                print(min(numbers[i:j-1]) + max(numbers[i:j-1]))
                return 0
            if curr_sum > sum or j == n: 
                break
            curr_sum = curr_sum + arr[j] 
            j += 1

subArraySum(numbers, 512, searched)