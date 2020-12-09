import json
import re

mandatory_elements = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def is_hex(s):
    return re.fullmatch(r"^[0-9a-fA-F]*$", s or "") is not None

def testEntry(data):
    if data[0] == "byr":
        return (1920 <= int(data[1]) <= 2002)
    elif data[0] == "iyr":
        return (2010 <= int(data[1]) <= 2020)
    elif data[0] == "eyr":
        return (2020 <= int(data[1]) <= 2030)
    elif data[0] == "hgt":
        unit = data[1][-2:]
        if unit == "cm":
            return 150 <= int(data[1][:-2]) <= 193
        if unit == "in":
            return 59 <= int(data[1][:-2]) <= 76
        else:
            return False
    elif data[0] == "hcl":
        return (data[1].startswith('#') and (len(data[1]) == 7) and is_hex(data[1][1:]))
    elif data[0] == "ecl":
        return data[1] in eye_colors
    elif data[0] == "pid":
        return (data[1].isdigit() and (len(data[1]) == 9))
    elif data[0] == "cid":
        return True
    else:
        return False

passports = []
with open ('day4/input.txt', 'r') as file:
    raw_input_data = file.read().replace("\n", " ").replace("  ", "\n").strip()
    for line in raw_input_data.split("\n"):
        passport = {}
        for entry in line.split(" "):
            data = entry.split(":")
            passport[data[0]] = data[1]
        passports.append(passport)

num_of_valid = 0

for passport in passports:
    valid = True
    for element in mandatory_elements:
        if element not in passport:
            valid = False
    if valid:
        num_of_valid +=1

print("Number of passports:", len(passports))
print("Valid passports:", num_of_valid)

num_of_valid2 = 0

for passport in passports:
    valid = True
    for element in mandatory_elements:
        if element not in passport:
            valid = False
    for entry in passport.items():
        if not testEntry(entry):
            valid = False
    if valid:
        num_of_valid2 +=1

print("Valid passports 2:", num_of_valid2)
print('Done with day 4!')