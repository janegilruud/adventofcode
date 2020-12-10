with open ('day10/input.txt', 'r') as file:
    input_data = [int(line.strip()) for line in file]

input_data.sort()

current_jolt = 0
one_jolt_step = 0
three_jolt_step = 1

num_arr = 1
one_step_streak = 0
three_streak = 0
four_streak = 0
five_streak = 0

# Since I count the streaks when I hit a 3-jolt-step
# I need to add the built-in joltage to the input data.
input_data.append(input_data[-1]+3)

for next_jolt in input_data:
    jolt_step = next_jolt - current_jolt
    if jolt_step == 1:
        one_jolt_step += 1
        one_step_streak += 1
    elif jolt_step == 3:
        three_jolt_step += 1
        if one_step_streak == 2:
            three_streak += 1
            num_arr = num_arr * 2
        elif one_step_streak == 3:
            four_streak += 1
            num_arr = num_arr * 4
        elif one_step_streak == 4:
            five_streak += 1
            num_arr = num_arr * 7
        elif one_step_streak > 5:
            print(one_step_streak,'step streak!')
        one_step_streak = 0

    current_jolt = next_jolt

print('One jolt steps:', one_jolt_step)
print('Three jolt steps:', three_jolt_step)
print('Product of one an three jolts steps:', one_jolt_step * three_jolt_step)

print('Three streak', three_streak, 'arrs:', 2**three_streak)
print('Four streak', four_streak, 'arrs:', 4**four_streak)
print('Five streak', five_streak, 'arrs:', 7**five_streak)
print('Arrs product:', (2**three_streak) * (4**four_streak) * (7**five_streak))
print('Number of arrangements is', num_arr)

print('Done with day 10!')
