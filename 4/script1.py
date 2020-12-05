passwords = []
commands = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
counter = 0

with open('input.txt') as file:
    data = file.read().split('\n\n')
    for line in data:
        passwordData = line.split()
        passwordDict = {}
        for field in passwordData:
            field = field.split(":")
            passwordDict[field[0]] = field[1]
        passwords.append(passwordDict)

for password in passwords:
    counter += 1
    for command in commands:
        if command not in password:
            counter -= 1
            break

print(counter)