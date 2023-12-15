data = open('Input.txt', 'r').read().split('\n')

maps = [[]]
answer = 0

for line in data:
    if len(line) == 0:
        maps.append([])
    else:
        maps[len(maps)-1].append(line)

def calculate_mirror_start(matches, edge_match):
    x, y = edge_match
    while x+1 != y and [x+1,y-1] in matches:
        x += 1
        y -=1
    return x+1 if x+1 == y else None

def calculate_mirror_value(map, forbidden_answer):
    row_count = len(map)
    col_count = len(map[0])
    
    row_matches = []
    for i in range(row_count):
        for j in range(i+1, row_count, 2):
            if all([map[i][k] == map[j][k] for k in range(col_count)]):
                row_matches.append([i, j])
    
    if len(row_matches) > 0:
        for edge_match in [x for x in row_matches if x[0] == 0 or x[1] == row_count - 1]:
            result = calculate_mirror_start(row_matches, edge_match)
            if result and (forbidden_answer == None or result * 100 != forbidden_answer):
                return result * 100
    
    column_matches = []
    for i in range(col_count):
        for j in range(i+1, col_count, 2):
            if all([map[k][i] == map[k][j] for k in range(row_count)]):
                column_matches.append([i, j])
    
    if len(column_matches) > 0:
        for edge_match in [x for x in column_matches if x[0] == 0 or x[1] == col_count - 1]:
            result = calculate_mirror_start(column_matches, edge_match)
            if result and (forbidden_answer == None or result != forbidden_answer):
                return result

def calculate_alternative_mirror_value(map, original_answer):
    for i in range(len(map)):
        for j in range(len(map[0])):
            alt_map = [[y for y in x] for x in map]
            alt_map[i][j] = '.' if alt_map[i][j] == '#' else '#'
            new_answer = calculate_mirror_value(alt_map, original_answer)
            
            if new_answer != None and new_answer != original_answer:
                return new_answer               

for map in maps:
    answer += calculate_alternative_mirror_value(map, calculate_mirror_value(map, None))

print(answer)