with open ('day3/input.txt', 'r') as file:
    input_data = [line.strip() for line in file]

slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
answer = 1

for slope in slopes:
    right = slope[0]
    down = slope[1]
    hits = 0
    for idx in range(0, len(input_data), down):
        row = input_data[idx]
        col = (int(idx/down) * right)
        col_mod = col%len(row)
        # print('Row', idx, ', col', col, '(', col_mod, ') ', row[col_mod], end='')
        if (row[col_mod] != '.'):
            # print(' HIT!')
            hits += 1
        # else:
            # print(' Miss')
    print('Number of hits: ', hits)
    answer = answer * hits

print('Second answer: ', answer)
print('Done with day 3!')