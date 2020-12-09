def findPair(numbers, total):
    if (total - numbers[0]) in numbers[1:]:
        return True
    if len(numbers) > 2:
        return findPair(numbers[1:], total)
    return False

with open ('day9/input.txt', 'r') as file:
    input_data = [int(line.strip()) for line in file]

idx = 0

while 1:
    preamble = input_data[idx:idx+25]
    weakness = input_data[idx+25]
    if not findPair(preamble, weakness):
        break
    idx+= 1

print('First weakness is:', weakness)

weakness_data = input_data[:idx]
idy = 0
length = 2

while 1:
    enc_range = weakness_data[idy:idy+length]
    enc_range.sort()
    if sum(enc_range) == weakness:
        print('Encryption weakness is:', enc_range[0] + enc_range[-1])
        break
    if idy >= idx:
        idy = 0
        length += 1
    else:
        idy += 1


print('Done with day 9!')
