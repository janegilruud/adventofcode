import copy

x_max = 0
y_max = 0

def neighboursAbove(array , x ,y):
    neighbours = 0
    if y:
        y0 = y-1
        left_side = x-1 if x else 0
        right_side = x+2 if x<=x_max else x_max
        neighbours = "".join(array[y0]).count('#', left_side, right_side)
    return neighbours

def neighboursBelow(array , x ,y):
    neighbours = 0
    if y < y_max:
        y0 = y+1
        left_side = x-1 if x else 0
        right_side = x+2 if x<=x_max else x_max
        neighbours = "".join(array[y0]).count('#', left_side, right_side)
    return neighbours

def neighboursSides(array , x ,y):
    neighbours = 0
    if x:
        if array[y][x-1] == '#':
            neighbours += 1
    if x < x_max:
        if array[y][x+1] == '#':
            neighbours += 1
    return neighbours

def countNeighbours(array , x ,y):
    return neighboursAbove(array, x, y) + neighboursBelow(array, x, y) + neighboursSides(array, x, y)

def newSeatState(array, x, y):
    nb = countNeighbours(array, x, y)
    current_state = array[y][x]
    if not nb:
        if current_state != '#':
            return True, '#'
    elif nb > 3:
        if current_state != 'L':
            return True, 'L'
    return False, current_state
    
def doIteration(array):
    new_array = copy.deepcopy(array)
    changes = False
    for y, row in enumerate(array):
        x = 0
        while x <= x_max:
            if array[y][x] != '.':
                change, state = newSeatState(array, x, y)
                if change:
                    changes = True
                    seats = new_array[y]
                    seats[x] = state
                    new_array[y] = seats
            x += 1
    return changes, new_array

with open ('day11/input.txt', 'r') as file:
    input_data = [list(line.strip().replace('L', '#')) for line in file]

x_max = len(input_data[0])-1
y_max = len(input_data)-1

iterations = 0

array_change = True

another_copy = copy.deepcopy(input_data)
while array_change:
    iterations += 1
    array_change, another_copy = doIteration(another_copy)

occupied_seats = 0
for line in another_copy:
    occupied_seats += "".join(line).count('#')

print('Number of iterations:', iterations)
print('Number of occupied seats:', occupied_seats)
print('Done with day 11!')