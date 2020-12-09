import copy
group_answers = []

with open ('day6/input.txt', 'r') as file:
    group_answer = []
    for line in file:
        if not line.strip():
            group_answers.append(copy.deepcopy(group_answer))
            group_answer = []
        else:
            group_answer.append(line.strip())

total_yes = 0

for group_answer in group_answers:
    yeses = []
    for answer in group_answer:
        for letter in answer:
            if letter not in yeses:
                yeses.append(letter)
    total_yes += len(yeses)

total_group_yes = 0

for group_answer in group_answers:
    group_yes = 0
    for letter in group_answer[0]:
        this_letter = True
        for answer in group_answer:
            if letter not in answer:
                this_letter = False
        if this_letter:
            group_yes += 1
    total_group_yes += group_yes

print('Total number of yes:', total_yes)
print('Total number of group yes:', total_group_yes)
print('Done with day 4!')