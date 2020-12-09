def testCode(inst_table):
    acc = 0
    idy = 0
    exed_inst = []
    while 1:
        if idy in exed_inst:
            return False, acc
        exed_inst.append(idy)
        inst = input_data[idy][0]
        if inst == 'acc':
            acc += int(input_data[idy][1])
            idy += 1
        elif inst == 'jmp':
            idy += int(input_data[idy][1])
        else:
            idy += 1
        if idy == len(input_data):
            return True, acc

with open ('day8/input.txt', 'r') as file:
    input_data = [line.strip().split(' ') for line in file]

success1, accum1 = testCode(input_data)
accum2 = 0

for idx, inst in enumerate(input_data):
    if inst[0] == 'nop':
        input_data[idx][0] = 'jmp'
        success,accum2 = testCode(input_data)
        if not success:
            input_data[idx][0] = 'nop'
    elif inst[0] == 'jmp':
        input_data[idx][0] = 'nop'
        success,accum2 = testCode(input_data)
        if not success:
            input_data[idx][0] = 'jmp'
        else:
            break

print('Accumulator1 is', accum1)
print('Accumulator2 is', accum2)

print('Done with day 8!')