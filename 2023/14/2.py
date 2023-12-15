data = tuple(map(tuple, [[y for y in x] for x in open('Input.txt', 'r').read().split('\n')]))
row_count = len(data)
past_answers = {}

def tilt_north(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] != 'O':
                continue
            
            i_track = i
            while i_track > 0 and data[i_track-1][j] == '.':
                data[i_track][j] = '.'
                i_track -= 1
                data[i_track][j] = 'O'
    return data

def tilt_south(data):
    for i in range(len(data))[::-1]:
        for j in range(len(data[0])):
            if data[i][j] != 'O':
                continue
            
            i_track = i
            while i_track < len(data) - 1 and data[i_track+1][j] == '.':
                data[i_track][j] = '.'
                i_track += 1
                data[i_track][j] = 'O'
    return data

def tilt_west(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] != 'O':
                continue
            
            j_track = j
            while j_track > 0 and data[i][j_track-1] == '.':
                data[i][j_track] = '.'
                j_track -= 1
                data[i][j_track] = 'O'
    return data

def tilt_east(data):
    for i in range(len(data)):
        for j in range(len(data[0]))[::-1]:
            if data[i][j] != 'O':
                continue
            
            j_track = j
            while j_track < len(data[0]) - 1 and data[i][j_track+1] == '.':
                data[i][j_track] = '.'
                j_track += 1
                data[i][j_track] = 'O'
    return data

def run_cycle(data):
    if data in past_answers:
        return past_answers[data]
    
    list_data = list(map(list, data))
    new_data = tilt_east(tilt_south(tilt_west(tilt_north(list_data))))
    tuple_new_data = tuple(map(tuple, new_data))
    
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