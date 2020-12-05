passwords = []
commands = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
eyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
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
    valid = True
    for command in commands:
        if command not in password:
            valid = False
            break
    if valid:
        if int(password['byr']) not in range(1920, 2003):
            valid = False
        if int(password['iyr']) not in range(2010, 2021):
            valid = False
        if int(password['eyr']) not in range(2020, 2031):
            valid = False

        if 'cm' in password['hgt']:
            password['hgt'] = password['hgt'].replace('cm', '')
            if int(password['hgt']) not in range(150, 194):
                valid = False
        elif 'in' in password['hgt']:
            password['hgt'] = password['hgt'].replace('in', '')
            if int(password['hgt']) not in range(59, 77):
                valid = False
            pass
        else:
            valid = False

        if password['hcl'][0] == "#":
            for i in range(1, 7):
                if password['hcl'][i] < '0' or password['hcl'][i] > 'f':
                    valid = False
        else:
            valid = False

        if password['ecl'] not in eyeColors:
            valid = False

        if len(password['pid']) != 9:
            valid = False

        if valid:
            counter += 1

print(counter)