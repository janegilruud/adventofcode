regulations = {}
regulations_nums = {}
my_bag = 'shiny gold'

def canContain(colour):
    if my_bag in regulations[colour]:
        return True
    else:
        for sub_colour in regulations[colour]:
            if canContain(sub_colour):
                return True
    return False

def containNumber(colour):
    num_of_bags = 0
    tot_sub_bags = 0
    sum_sub_bags = 0
    for idx, sub_colour in enumerate(regulations[colour]):
        sub_bags = containNumber(sub_colour)
        if sub_bags:
            sum_sub_bags += regulations_nums[colour][idx] * sub_bags

    for num in regulations_nums[colour]:
        num_of_bags += num
    tot_sub_bags = num_of_bags + sum_sub_bags
    # print('Number of bags in', colour, ':', tot_sub_bags)
    return tot_sub_bags


with open ('day7/input.txt', 'r') as file:
    input_data = [line.strip().split(' bags contain ') for line in file]
    for entry in input_data:
        split_entry = entry[1].split(' ')
        regulations[entry[0]] = []
        regulations_nums[entry[0]] = []
        for idx, thing in enumerate(split_entry):
            if split_entry[idx].isdecimal():
                regulations[entry[0]].append(' '.join(split_entry[idx+1:idx+3]))
                regulations_nums[entry[0]].append(int(split_entry[idx]))

can_contain_golden = 0

for regulation in regulations:
    if canContain(regulation):
        can_contain_golden += 1



print('Number of bags that can contain golden shiny:',can_contain_golden)
print('Number of bags that a golden shiny bag contains:',containNumber(my_bag))
print('Done with day 7!')