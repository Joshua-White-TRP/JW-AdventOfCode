data = open('Input.txt', 'r').read().split('\n')
num_to_dir = { 0: 'R', 1: 'D', 2: 'L', 3: 'U' }

dig_coords = [[0, 0]]
perimeter = 1
for line in data:
    orig_direction, orig_length_text, color = line.split(' ')
    hex_num = color[2:len(color)-2]
    hex_dir = color[-2]
    
    length = int(hex_num, 16)
    perimeter += length
    
    nx, ny = dig_coords[-1]
    match num_to_dir[int(hex_dir)]:
        case 'R': ny += length
        case 'D': nx += length
        case 'L': ny -= length
        case 'U': nx -= length
    dig_coords.append([nx, ny])

interior_x, interior_y = 0, 0
for i in range(1, len(dig_coords)):
    a = dig_coords[i-1]
    b = dig_coords[i]
    interior_x += a[0] * b[1]
    interior_y += a[1] * b[0]
interior = abs(interior_x - interior_y)

print(int((perimeter + interior) / 2 + 0.5))