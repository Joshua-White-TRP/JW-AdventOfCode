data = tuple(map(tuple, [[y for y in x] for x in open('Input.txt', 'r').read().split('\n')]))
row_count = len(data)
past_answers = {}

#This function works but is not very legible. Attempt at generifying the tilt function.
#Less lines of code but all the additional conditions result in a slower program (about 33% slower on my machine).
def tilt(data, is_by_row, reverse):
    for i in range(len(data))[::(-1 if is_by_row and reverse else 1)]:
        for j in range(len(data[0]))[::(-1 if not is_by_row and reverse else 1)]:
            if data[i][j] != 'O':
                continue
            
            track = i if is_by_row else j
            additive = -1 if not reverse else 1
            while (track > 0 if not reverse else track < len(data)-1 if is_by_row else track < len(data[0])-1) and data[track+additive if is_by_row else i][track+additive if not is_by_row else j] == '.':
                data[track if is_by_row else i][track if not is_by_row else j] = '.'
                track += additive
                data[track if is_by_row else i][track if not is_by_row else j] = 'O'
    return data


def run_cycle(data):
    if data in past_answers:
        return past_answers[data]
    
    north_tilted_data = tilt(list(map(list, data)), True, False)
    west_tilted_data = tilt(north_tilted_data, False, False)
    south_tilted_data = tilt(west_tilted_data, True, True)
    east_tilted_data = tilt(south_tilted_data, False, True)
    tuple_new_data = tuple(map(tuple, east_tilted_data))
    
    past_answers[data] = tuple_new_data
    return tuple_new_data

iterations = 1000000000
first_repeat = None
first_repeat_index = None
second_repeat_index = None
for i in range(iterations):
    if data in past_answers:
        data = past_answers[data]
        
        if first_repeat != None and data == first_repeat:
            second_repeat_index = i
            break
            
        if first_repeat_index == None:
            first_repeat = data
            first_repeat_index = i
    else:
        data = run_cycle(data)

for i in range((iterations - 1 - first_repeat_index) % (second_repeat_index - first_repeat_index)):
    data = run_cycle(data)

answer = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 'O':
            answer += row_count - i

print(answer)