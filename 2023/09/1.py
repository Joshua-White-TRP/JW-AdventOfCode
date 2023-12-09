data = open('Input.txt', 'r').read().split('\n')

number_lists = [[int(y) for y in x.split(' ')] for x in data]
answer = 0

for number_list in number_lists:
    previous_sequence = number_list
    addition = 0
    
    while len([x for x in previous_sequence if x != 0]) > 0:
        addition += previous_sequence[len(previous_sequence) - 1]
        previous_sequence = [previous_sequence[idx + 1] - x for idx, x in enumerate(previous_sequence[:-1])]
    
    answer += addition
    
print(answer)