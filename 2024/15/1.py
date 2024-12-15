data = open('Input.txt', 'r').read().split('\n')
ds = {
    '^': [-1,0],
    '>': [0,1],
    'v': [1,0],
    '<': [0,-1]
}

map = []
directions = []
is_mapping = True
for line in data:
    if line == '':
        is_mapping = False
    
    if is_mapping:
        map.append([x for x in line])
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
    n_pos = [t_pos[0] + d[0], t_pos[1] + d[1]]
    n_symbol = map[n_pos[0]][n_pos[1]]
    
    if n_symbol == '.' or (n_symbol == 'O' and push(n_pos, d)):
        map[t_pos[0]][t_pos[1]] = '.'
        map[n_pos[0]][n_pos[1]] = 'O'
        return True
    return False

for d in directions:
    n_pos = [r_pos[0] + d[0], r_pos[1] + d[1]]
    n_symbol = map[n_pos[0]][n_pos[1]]
    
    if n_symbol == '.' or (n_symbol == 'O' and push(n_pos, d)):
        map[r_pos[0]][r_pos[1]] = '.'
        map[n_pos[0]][n_pos[1]] = '@'
        r_pos = n_pos

ans = 0
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == 'O':
            ans += y * 100 + x
print(ans)
