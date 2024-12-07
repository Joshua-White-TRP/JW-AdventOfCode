data = open('Input.txt', 'r').read().split('\n')
d = [[-1,0],[0,1],[1,0],[0,-1]]
starting_pos = None
ans = 0

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == '^':
            starting_pos = (y,x,0)
            break
    if starting_pos != None:
        break

def search(iter_data):
    visited_locations = set()
    cur_pos = starting_pos
    d_idx = 0

    while cur_pos[0] >= 0 and cur_pos[0] < len(iter_data) and cur_pos[1] >= 0 and cur_pos[1] < len(iter_data[0]):
        visited_locations.add(cur_pos)
        
        while True:
            cur_d_idx = d_idx % 4
            new_pos = (cur_pos[0] + d[cur_d_idx][0], cur_pos[1] + d[cur_d_idx][1], cur_d_idx)
            if new_pos[0] < 0 or new_pos[0] >= len(iter_data) or new_pos[1] < 0 or new_pos[1] >= len(iter_data[0]) or iter_data[new_pos[0]][new_pos[1]] != '#':
                if new_pos in visited_locations:
                    return 1
                cur_pos = new_pos
                break
            else:
                d_idx += 1
    return {(v[0], v[1]) for v in visited_locations}

for p in search(data):
    search_result = search([''.join(['#' if p[0] == idx_y and p[1] == idx_x else x for idx_x, x in enumerate(y)]) for idx_y, y in enumerate(data)])
    if search_result == 1:
        ans += 1
print(ans)