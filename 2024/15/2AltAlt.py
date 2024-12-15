data = open('Input.txt', 'r').read().split('\n')
b_arr = ['[',']']
ds = { '^': [-1,0], '>': [0,1], 'v': [1,0], '<': [0,-1] }
tiles = { '#': ['#','#'], 'O': b_arr, '.': ['.','.'], '@': ['@','.'] }

map, directions, is_mapping = [], [], True
for line in data:
    if line == '':
        is_mapping = False
    
    if is_mapping:
        row = [tiles[x] for x in line]
        map.append([item for arr in row for item in arr])
    else:
        directions.extend([ds[x] for x in line])

r_pos = None
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == '@':
            r_pos = [y,x]
    if r_pos != None:
        break

def horizontal_search(p, d):
    symbol = map[p[0]][p[1]]
    if symbol == '#':
        return False
    elif symbol == '.':
        return []
    else:
        ans = horizontal_search([p[0], p[1] + d[1]], d)
        return False if ans == False else [p] + ans

def vertical_search(box_positions, d):
    above_positions = [[x[0] + d[0], x[1]] for x in box_positions]
    above_positions = [[x[0], x[1], map[x[0]][x[1]]] for x in above_positions if map[x[0]][x[1]] != '.']
    if '#' in [x[2] for x in above_positions]:
        return False
    if len(above_positions) == 0:
        return []
    
    for a in above_positions:
        new_value = [a[0], a[1] + 1, ']'] if a[2] == '[' else [a[0], a[1] - 1, '[']
        
        if not any([x[0] == new_value[0] and x[1] == new_value[1] for x in above_positions]):
            above_positions.append(new_value)
    
    n = vertical_search(above_positions, d)
    return False if n == False else above_positions + n

for d in directions:
    n_pos = [r_pos[0] + d[0], r_pos[1] + d[1]]
    n_symbol = map[n_pos[0]][n_pos[1]]
    
    if n_symbol == '.':
        map[r_pos[0]][r_pos[1]] = '.'
        map[n_pos[0]][n_pos[1]] = '@'
        r_pos = n_pos
    elif n_symbol != '#':
        if d in [ds['>'], ds['<']]:
            res = horizontal_search(r_pos, d)
            if res:
                for r in res[::-1]:
                    map[r[0]][r[1] + d[1]] = map[r[0]][r[1]]
                map[r_pos[0]][r_pos[1]], r_pos = '.', n_pos
        else:
            res = vertical_search([r_pos], d)
            if res:
                for r in res[::-1]:
                    map[r[0] + d[0]][r[1]] = r[2]
                    map[r[0]][r[1]] = '.'
                map[r_pos[0]][r_pos[1]] = '.'
                map[n_pos[0]][n_pos[1]] = '@'
                r_pos = n_pos

ans = 0
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == '[':
            ans += y * 100 + x
print(ans)