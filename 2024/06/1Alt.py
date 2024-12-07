data = [[y for y in x] for x in open('Input.txt', 'r').read().split('\n')]
directions = []
d = [[-1,0],[0,1],[1,0],[0,-1]]

cur_pos = None
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == '^':
            cur_pos = (y,x,0)
            break
    if cur_pos != None:
        break

def is_in_range(data, y, x):
    return x >= 0 and y >= 0 and y < len(data) and x < len(data[0])

while is_in_range(data, cur_pos[0], cur_pos[1]):
    y, x, cur_d_idx = cur_pos
    cur_d = d[cur_d_idx]
    while is_in_range(data, y, x):
        y += cur_d[0]
        x += cur_d[1]
        
        if not is_in_range(data, y, x):
            directions.append((cur_pos, (y - cur_d[0], x - cur_d[1], cur_d_idx)))
            cur_pos = (y, x, cur_d_idx)
            break
        elif data[y][x] == '#':
            new_pos = (y - cur_d[0], x - cur_d[1], (cur_d_idx + 1) % 4)
            directions.append((cur_pos, new_pos, cur_d_idx))
            cur_pos = new_pos
            break

ans = 0
for dir in directions:
    y1, y2, = sorted([dir[0][0], dir[1][0]])
    x1, x2 = sorted([dir[0][1], dir[1][1]])
    
    for y in [y for y in range(y1, y2+1)]:
        for x in [x for x in range(x1, x2+1) if data[y][x] != 'O']:
            data[y][x] = 'O'
            ans += 1

[print(''.join(x)) for x in data]
print(ans)