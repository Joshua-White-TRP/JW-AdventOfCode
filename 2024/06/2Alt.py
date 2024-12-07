data = [[y for y in x] for x in open('Input.txt', 'r').read().split('\n')]
d = [[-1,0],[0,1],[1,0],[0,-1]]
attempted_blockages = []
successful_blockages = []

start_pos = None
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == '^':
            start_pos = (y,x,0)
            break
    if start_pos != None:
        break

def is_in_range(data, y, x):
    return x >= 0 and y >= 0 and y < len(data) and x < len(data[0])

def search(cur_pos, blocked_position):
    walls = []
    y, x, d_idx = cur_pos
    while True:
        new_y, new_x = y + d[d_idx][0], x + d[d_idx][1]
        if not is_in_range(data, new_y, new_x):
            return
        
        new_pos = [new_y,new_x]
        char = data[new_y][new_x]
        if char == '#':
            wall = (new_y, new_x, d_idx)
            if wall in walls:
                successful_blockages.append(blocked_position)
                return
            walls.append(wall)
            d_idx = (d_idx + 1) % 4
            continue
        elif blocked_position == None and char == '.' and new_pos not in attempted_blockages:
            data[new_y][new_x] = '#'
            attempted_blockages.append(new_pos)
            search((y, x, d_idx), new_pos)
            data[new_y][new_x] = '.'
        
        y, x = new_y, new_x

search((start_pos[0], start_pos[1], start_pos[2]), None)
print(len(set([(x[0], x[1]) for x in successful_blockages])))