data = [[y for y in x] for x in open('Input.txt', 'r').read().split('\n')]
fslash_map = { 'E':'N', 'N':'E', 'W':'S', 'S':'W' }
bslash_map = { 'E':'S', 'S':'E', 'W':'N', 'N':'W' }
energised_locations = []

row_count = len(data)
col_count = len(data[0])

def move_by_direction(current_location, direction):
    new_location = current_location.copy()
    match direction:
        case 'S': new_location[0] += 1
        case 'N': new_location[0] -= 1
        case 'E': new_location[1] += 1
        case 'W': new_location[1] -= 1
    return new_location

def save_energised_locations(current_location, direction):
    while current_location[0] >= 0 and current_location[0] < row_count and current_location[1] >= 0 and current_location[1] < col_count and [current_location, direction] not in energised_locations:
        energised_locations.append([current_location.copy(), direction])
        char = data[current_location[0]][current_location[1]]
        
        match char:
            case '/': direction = fslash_map[direction]
            case '\\': direction = bslash_map[direction]
            case '|':
                if direction in ['E', 'W']:
                    save_energised_locations(move_by_direction(current_location, 'S'), 'S')
                    save_energised_locations(move_by_direction(current_location, 'N'), 'N')
                    return
            case '-':
                if direction in ['N', 'S']:
                    save_energised_locations(move_by_direction(current_location, 'E'), 'E')
                    save_energised_locations(move_by_direction(current_location, 'W'), 'W')
                    return
        
        current_location = move_by_direction(current_location, direction)

save_energised_locations([0, 0], 'E')
answer = len(set([tuple(x) for x in [y[0] for y in energised_locations]]))
print(answer)