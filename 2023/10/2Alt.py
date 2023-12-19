import sys
data = open('Input.txt', 'r').read().split('\n')
sys.setrecursionlimit(10000)

row_count = len(data)
column_count = len(data[0])
loop_coords = set()
current_coords = ()
prev_coords = ()
current_char = 'S'

for i in range(row_count):
    for j in range(column_count):
        if data[i][j] == 'S':
            current_coords = (i, j)
            prev_coords = (-1, -1)

valid_char_mappings = [[['S', '|', 'L', 'J'],['S', '|', '7', 'F']], [['S', '|', '7', 'F'],['S', '|', 'L', 'J']], [['S', '-', 'J', '7'],['S', '-', 'L', 'F']], [['S', '-', 'L', 'F'],['S', '-', 'J', '7']]]

while current_char != 'S' or len(loop_coords) == 0:
    indexes_to_check = [(current_coords[0] - 1, current_coords[1]), (current_coords[0] + 1, current_coords[1]), (current_coords[0], current_coords[1] - 1), (current_coords[0], current_coords[1] + 1)]
    loop_coords.add(current_coords)
    
    for idx, i in enumerate(indexes_to_check):
        if i[0] < 0 or i[0] >= row_count or i[1] < 0 or i[1] >= column_count or (prev_coords[0] == i[0] and prev_coords[1] == i[1]):
            continue;
        
        if current_char in valid_char_mappings[idx][0] and data[i[0]][i[1]] in valid_char_mappings[idx][1]:
            prev_coords = current_coords
            current_coords = i
            break
    
    current_char = data[current_coords[0]][current_coords[1]]

alternate_map = []
for i in range(row_count):
    recreated_row = []
    gap_row = []
    
    for j in range(column_count):
        recreated_row.append(data[i][j])
        
        if (i, j) in loop_coords and (i, j+1) in loop_coords and data[i][j] in valid_char_mappings[3][0] and data[i][j+1] in valid_char_mappings[3][1]:
            recreated_row.append('-')
        else:
            recreated_row.append(' ')
        
        if (i, j) in loop_coords and (i+1, j) in loop_coords and data[i][j] in valid_char_mappings[1][0] and data[i+1][j] in valid_char_mappings[1][1]:
            gap_row.append('|')
        else:
            gap_row.append(' ')
        
        gap_row.append(' ')
    alternate_map.append(recreated_row)
    alternate_map.append(gap_row)

def get_adjacent_locations(i, j):
    return [
        [i-1,j-1],[i-1,j],[i-1,j+1],
        [i,j-1],[i,j+1],
        [i+1,j-1],[i+1,j],[i+1,j+1],
    ]

def is_map_pipe(i, j):
    if alternate_map[i][j] == ' ':
        return False

    for adjacent_location in [x for x in get_adjacent_locations(i, j) if x[0] >= 0 and x[1] >= 0 and x[0] < len(alternate_map) and x[1] < len(alternate_map[0])]:
        if alternate_map[adjacent_location[0]][adjacent_location[1]] != ' ':
            return True
    return False

update_locs = {}
invalid_locations = {}
def evaluate_location(i, j, history):
    if i < 0 or i >= len(alternate_map) or j < 0 or j >= len(alternate_map[0]) or alternate_map[i][j] == 'O':
        update_locs.add((i, j))
        return 'O'
    elif alternate_map[i][j] == 'I':
        update_locs.add((i, j))
        return 'I'
    elif is_map_pipe(i, j):
        invalid_locations.add((i, j))
        return None
    else:
        update_locs.add((i, j))
        adjacent_locations = get_adjacent_locations(i, j)
        for adjacent_location in [x for x in adjacent_locations if x not in history and (x[0], x[1]) not in invalid_locations]:
            result = evaluate_location(adjacent_location[0], adjacent_location[1], history + [[i, j]])
            if result != None:
                return result 
        
        invalid_locations.add((i, j))
        return None

for i in range(len(alternate_map)):
    for j in range(len(alternate_map[0])):
        if alternate_map[i][j] == ' ' or is_map_pipe(i, j):
            continue
        
        invalid_locations = {(i,j)}
        update_locs = {(i, j)}
        result = evaluate_location(i, j, [])
        
        true_result = 'I' if result == None else result
        for loc in update_locs:
            alternate_map[loc[0]][loc[1]] = true_result

inner_count = 0
for i in range(len(alternate_map))[::2]:
    for j in range(len(alternate_map[0]))[::2]:
        if alternate_map[i][j] == 'I':
            inner_count += 1

for idx, x in enumerate(alternate_map):
    alternate_map[idx] = ''.join(x)

print(inner_count)














