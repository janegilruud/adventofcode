with open ('day1/input.txt', 'r') as file:
    input_data = [int(line.strip()) for line in file]

for idx, num1 in enumerate(input_data):
    data_slice = input_data[(idx+1):(len(input_data)-1):1]
    matching_num = 2020 - num1
    for idy, num2 in enumerate(data_slice):
        if num2 == matching_num:
            print("The numbers are: ", num1, " and ", num2)
            print("(index ", idx, " and ", idx+idy, ")")
            print("Today's first solution is : ", num1 * num2)

for idx, num1 in enumerate(input_data):
    data_slice_y = input_data[(idx+1):(len(input_data)-1):1]
    for idy, num2 in enumerate(data_slice_y):
        data_slice_z = data_slice_y[(idx+1):(len(data_slice_y)-1):1]
        for idz, num3 in enumerate(data_slice_z):
            if 2020 == (num1 + num2 + num3):
                print("The numbers are: ", num1, ", ", num2, " and ", num3)
                print("(index ", idx, ", ", idx+idy, " and ", idx+idy+idz, ")")
                print("Today's second solution is : ", num1 * num2 * num3)


print('Done with day 1!')