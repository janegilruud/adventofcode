curr_dir = 'E'
pos_e = 0
pos_n = 0
wp_e = 10
wp_n = 1

directions = ['N', 'E', 'S', 'W']

def moveShip(direction, distance):
    global pos_e, pos_n
    if direction == 'N':
        pos_n += distance
    elif direction == 'E':
        pos_e += distance
    elif direction == 'S':
        pos_n -= distance
    elif direction == 'W':
        pos_e -= distance

def swingShip(side, degrees):
    global curr_dir
    steps = degrees/90
    idx = directions.index(curr_dir)
    if side == 'L':
        steps = -steps
    new_idx = idx + steps
    if new_idx < 0:
        new_idx += 4
    elif new_idx > 3:
        new_idx -= 4
    curr_dir = directions[int(new_idx)]

def moveShipWp(times):
    global pos_e, pos_n
    pos_e += (wp_e * times)
    pos_n += (wp_n * times)

def moveWp(direction, distance):
    global wp_e, wp_n
    if direction == 'N':
        wp_n += distance
    elif direction == 'E':
        wp_e += distance
    elif direction == 'S':
        wp_n -= distance
    elif direction == 'W':
        wp_e -= distance

def swingWp(side, degrees):
    global wp_e, wp_n
    if degrees == 180:
        new_wp_e = -wp_e
        new_wp_n = -wp_n
    else:
        to_left = (side == 'L')
        if degrees == 270:
            to_left = not to_left
        if(to_left):
            new_wp_e = -wp_n
            new_wp_n = wp_e
        else:
            new_wp_e = wp_n
            new_wp_n = -wp_e
    wp_e = new_wp_e
    wp_n = new_wp_n

with open ('day12/input.txt', 'r') as file:
    input_data = []
    for line in file:
        line.strip()
        letter = line[0]
        number = int(line[1:])
        input_data.append([letter, number])

# Part 1
for instr in input_data:
    if instr[0] == 'F':
        moveShip(curr_dir, instr[1])
    elif instr[0] in directions:
        moveShip(instr[0], instr[1])
    else:
        swingShip(instr[0], instr[1])

print('Position (N', pos_n, ') (E', pos_e, '), distance', abs(pos_e + pos_n))

# Part 2
curr_dir = 'E'
pos_e = 0
pos_n = 0

for instr in input_data:
    if instr[0] == 'F':
        moveShipWp(instr[1])
    elif instr[0] in directions:
        moveWp(instr[0], instr[1])
    else:
        swingWp(instr[0], instr[1])

print('Position (N', pos_n, ') (E', pos_e, '), distance', abs(pos_e + pos_n))

print('Done with day12!')