import copy

x_max = 0
y_max = 0

def countOccupiedSeats(array):
    occupied_seats = 0
    for line in array:
        occupied_seats += "".join(line).count('#')
    return occupied_seats

def nextSeatInDir(x_step, y_step, x, y, array, look_far):
    if not (x_step or y_step):
        return 0
    x_new = x
    y_new = y
    while look_far:
        x_new += x_step
        y_new += y_step
        if not (0 <= x_new <= x_max) or not (0 <= y_new <= y_max):
            return 0
        elif array[y_new][x_new] == '#':
            return 1
        elif array[y_new][x_new] == 'L':
            return 0
        if look_far > 0:
            look_far -= 1
    return 0

def newSeatState(array, x, y, look_far, max_nb):
    x_dir = [-1, 0, 1]
    y_dir = [-1, 0, 1]

    current_state = array[y][x]
    neighbours = 0
    for y_step in y_dir:
        for x_step in x_dir:
            neighbours += nextSeatInDir(x_step, y_step, x, y, array, look_far)

    if not neighbours:
        if current_state != '#':
            return True, '#'
    elif neighbours >= max_nb:
        if current_state != 'L':
            return True, 'L'
    return False, current_state
    
def doIteration(array, look_far, max_nb):
    new_array = copy.deepcopy(array)
    changes = False
    for y, row in enumerate(array):
        x = 0
        while x <= x_max:
            if array[y][x] != '.':
                change, state = newSeatState(array, x, y, look_far, max_nb)
                if change:
                    changes = True
                    seats = new_array[y]
                    seats[x] = state
                    new_array[y] = seats
            x += 1
    return changes, new_array

def runShow(array, look_far, max_nb):
    iterations = 0
    array_change = True
    while array_change:
        iterations += 1
        array_change, array = doIteration(array, look_far, max_nb)
    return iterations, array

with open ('day11/input.txt', 'r') as file:
    input_data = [list(line.strip().replace('L', '#')) for line in file]

x_max = len(input_data[0])-1
y_max = len(input_data)-1

first_iter, first_array = runShow(input_data, 1, 4)

print('Number of iterations in part 1:', first_iter)
print('Number of occupied seats in part 1:', countOccupiedSeats(first_array))

second_iter, second_copy = runShow(input_data, -1, 5)

print('Number of iterations in part 2:', second_iter)
print('Number of occupied seats in part 2:', countOccupiedSeats(second_copy))

print('Done with day 11!')