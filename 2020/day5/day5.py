def getPlace(letters, region):
    middle = int(len(region)/2)
    if letters[0] in ('F', 'L'):
        new_region = region[:middle]
    else:
        new_region = region[middle:]
    if len(letters) > 1:
        return getPlace(letters[1:], new_region)
    else:
        return new_region[0]

max_id = 0
ids = []

with open ('day5/input.txt', 'r') as file:
    input_data = [line.strip() for line in file]

for code in input_data:
    row = getPlace(code[:7], list(range(128)))
    column = getPlace(code[7:], list(range(8)))

    id = row * 8 + column
    ids.append(id)
    max_id = max(id, max_id)

ids.sort()
idx = 0
while idx < (len(ids)-1):
    if (ids[idx+1]) == (ids[idx] + 2):
        seat = ids[idx] + 1
    idx +=1
print('Highest ID: ', max_id)
print('Seat is: ', seat)
print('Done with day 5!')