data = open('Input.txt', 'r').read().split('\n')
visited_locations = set()
d = [[-1,0],[0,1],[1,0],[0,-1]]
d_idx = 0

cur_pos = None
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == '^':
            cur_pos = (y,x)
            break
    if cur_pos != None:
        break

while cur_pos[0] >= 0 and cur_pos[0] < len(data) and cur_pos[1] >= 0 and cur_pos[1] < len(data[0]):
    visited_locations.add(cur_pos)
    
    while True:
        new_pos = (cur_pos[0] + d[d_idx % 4][0], cur_pos[1] + d[d_idx % 4][1])
        if new_pos[0] < 0 or new_pos[0] >= len(data) or new_pos[1] < 0 or new_pos[1] >= len(data[0]) or data[new_pos[0]][new_pos[1]] != '#':
            cur_pos = new_pos
            break
        else:
            d_idx += 1

for x in range(len(data)):
    print(''.join([y if y == '^' or (x, idx) not in visited_locations else 'O' for idx, y in enumerate(data[x])]))
print(len(visited_locations))