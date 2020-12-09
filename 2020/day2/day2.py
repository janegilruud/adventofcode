with open ('day2/input.txt', 'r') as file:
    input_data = [line.strip().split(' ') for line in file]

num_passwd = 0
valid_passwords = 0
nonvalid_passwords = 0
valid_passw2 = 0
nonvalid_passw2 = 0

for data in input_data:
    num_passwd += 1
    minmax = list(map(int, data[0].split('-')))
    letter = data[1][0]
    letter_count = data[2].count(letter)
    if int(minmax[0]) <= letter_count <= int(minmax[1]):
        valid_passwords += 1
    else:
        nonvalid_passwords += 1

    first = minmax[0]-1
    second = minmax[1]-1

    if data[2][first] != data[2][second]:
        if data[2][first] is letter or data[2][second] is letter:
            valid_passw2 += 1
        else:
            nonvalid_passw2 += 1
    else:
        nonvalid_passw2 += 1

print("Number of passwords: ", num_passwd)
print("Number of valid passwords: ", valid_passwords)
print("Number of non-valid passwords: ", nonvalid_passwords)
print("Number of valid passwords 2: ", valid_passw2)
print("Number of non-valid passwords 2: ", nonvalid_passw2)

print('Done with day 2!')