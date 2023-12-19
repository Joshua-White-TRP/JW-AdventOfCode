data = open('Input.txt', 'r').read().split('\n')
directions = { 'R': (0, 1), 'L': (0, -1), 'D': (1, 0), 'U': (-1, 0) }
coord = [0, 0]

digs = []
for line in data:
    direction, length, color = line.split(' ')
    digs.append((direction, int(length)))

map = [['#']]
for direction, length in digs:
    for i in range(length):
        nx, ny = coord[0] + directions[direction][0], coord[1] + directions[direction][1]
        
        if nx < 0:
            map.insert(0, [])
            nx = 0
        elif ny < 0:
            ny = 0
            for m in map:
                m.insert(0, '-')
        
        if len(map) <= nx:
            map.append([])
        
        while len(map[nx]) <= ny:
            map[nx].append('-')
        
        map[nx][ny] = '#'
        coord = [nx, ny]

for idx, cell in enumerate(map[0]):
    if cell == '#' and map[1][idx] != '#':
        flood_start_coord = (1,idx)
        break

def get_adjacent_locations(i, j):
    return [
        [i-1,j-1],[i-1,j],[i-1,j+1],
        [i,j-1],[i,j+1],
        [i+1,j-1],[i+1,j],[i+1,j+1]
    ]

queue = [flood_start_coord]
visited = {(flood_start_coord)}
while queue:
    cx, cy = queue.pop()
    map[cx][cy] = '#'
    adjacent_coords = get_adjacent_locations(cx, cy)
    for ax, ay in adjacent_coords:
        if not (ax < 0 or ay < 0 or ax >= len(map) or ay >= len(map[ax]) or map[ax][ay] == '#' or (ax,ay) in visited):
            queue.append((ax, ay))
            visited.add((ax, ay))

ans = 0
for row in map:
    for cell in row:
        if cell == '#':
            ans += 1
[print(''.join(x)) for x in map]
print(ans)