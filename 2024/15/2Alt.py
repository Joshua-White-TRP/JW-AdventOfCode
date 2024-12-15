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

def push(t_pos, d):
    t_symbol = map[t_pos[0]][t_pos[1]]
    t_pos2 = [t_pos[0], t_pos[1] + (d[1] if d[1] != 0 else -1 if t_symbol == ']' else 1)] 
    t_symbol2 = map[t_pos2[0]][t_pos2[1]]
    
    n_pos, n_pos2 = [t_pos[0] + d[0], t_pos[1] + d[1]], [t_pos2[0] + d[0], t_pos2[1] + d[1]]
    n_symbol, n_symbol2 = map[n_pos[0]][n_pos[1]], map[n_pos2[0]][n_pos2[1]]
    ret_arr = [[t_pos, t_pos2, n_pos, n_pos2, t_symbol, t_symbol2]]
    is_horizontal = d == ds['>'] or d == ds['<']
    
    if n_symbol == '#' or n_symbol2 == '#':
        return False
    if (n_symbol == '.' and n_symbol2 == '.') or (is_horizontal and n_symbol2 == '.'):
        return ret_arr
    
    n_push, n_push2 = push(n_pos, d), push(n_pos2, d) 
    if (is_horizontal and n_push2) or (n_symbol == '.' and n_push2):
        [ret_arr.append(x) for x in n_push2]
    elif (n_symbol2 == '.' and n_push) or (t_symbol == n_symbol and n_push):
        [ret_arr.append(x) for x in n_push]
    elif n_push and n_push2:
        [ret_arr.append(x) for x in n_push]
        [ret_arr.append(x) for x in n_push2]
    
    return False if len(ret_arr) == 1 else ret_arr

for d in directions:
    n_pos = [r_pos[0] + d[0], r_pos[1] + d[1]]
    n_symbol = map[n_pos[0]][n_pos[1]]
    res = True if n_symbol == '.' else push(n_pos, d) if n_symbol != '#' else False
    
    if res:
        if isinstance(res, list):
            if d in [ds['^'], ds['v']]:
                res.sort(key=lambda x: x[2][0], reverse = d == ds['^'])
            
            for i in res[::-1]:
                t_pos, t_pos2, a_pos, a_pos2, t_symbol, t_symbol2 = i
                map[t_pos[0]][t_pos[1]] = '.'
                map[t_pos2[0]][t_pos2[1]] = '.'
                map[a_pos[0]][a_pos[1]] = t_symbol
                map[a_pos2[0]][a_pos2[1]] = t_symbol2
        map[r_pos[0]][r_pos[1]] = '.'
        map[n_pos[0]][n_pos[1]] = '@'
        r_pos = n_pos
[print(''.join(r)) for r in map]

ans = 0
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == '[':
            ans += y * 100 + x
print(ans)