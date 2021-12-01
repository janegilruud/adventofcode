with open ('2021/day1/input.txt', 'r') as file:
    input_data = [int(line.strip()) for line in file]

data_size = len(input_data)
incr_depth = 0
index = 1
while index < data_size:
    if input_data[index] > input_data[index-1]:
        incr_depth += 1
    index += 1

print("Part 1: The number of measurments larger than the previous: ", incr_depth)


incr_depth = 0
index = 3
prev_measure = input_data[0] + input_data[1] + input_data[2]
while index < data_size:
    new_measure = prev_measure + input_data[index] - input_data[index-3]
    if new_measure > prev_measure:
        incr_depth += 1
    index += 1

print("Part 2: The number of measurments larger than the previous: ", incr_depth)