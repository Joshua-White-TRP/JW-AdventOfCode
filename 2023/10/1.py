data = open('Input.txt', 'r').read().split('\n')

row_count = len(data)
column_count = len(data[0])
current_coords = []
prev_coords = []
current_char = 'S'

for i in range(row_count):
    for j in range(column_count):
        if data[i][j] == 'S':
            current_coords = [i, j]
            prev_coords = [-1, -1]

valid_char_mappings = [[['S', '|', 'L', 'J'],['S', '|', '7', 'F']], [['S', '|', '7', 'F'],['S', '|', 'L', 'J']], [['S', '-', 'J', '7'],['S', '-', 'L', 'F']], [['S', '-', 'L', 'F'],['S', '-', 'J', '7']]]
loop_steps = 0

while current_char != 'S' or loop_steps == 0:
    index_adjustment = 1
    indexes_to_check = [[current_coords[0] - 1, current_coords[1]], [current_coords[0] + 1, current_coords[1]], [current_coords[0], current_coords[1] - 1], [current_coords[0], current_coords[1] + 1]]
    
    for idx, i in enumerate(indexes_to_check):
        if i[0] < 0 or i[0] >= row_count or i[1] < 0 or i[1] >= column_count or (prev_coords[0] == i[0] and prev_coords[1] == i[1]):
            continue;
        
        if current_char in valid_char_mappings[idx][0] and data[i[0]][i[1]] in valid_char_mappings[idx][1]:
            prev_coords = current_coords
            current_coords = i
            break
    
    loop_steps += 1
    current_char = data[current_coords[0]][current_coords[1]]
    
print(loop_steps // 2)