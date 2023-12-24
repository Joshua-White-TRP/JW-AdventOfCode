data = [[y for y in x] for x in open('Input.txt', 'r').read().split('\n')]
cardinal_moves = [(-1,0),(0,1),(1,0),(0,-1)]
row_count = len(data)
col_count = len(data)
s_coords = (row_count//2, col_count//2)

def map_steps_to_locations(start, starting_parity):
    visited = set()
    step_map = {}
    q = [[start, 0]]
    last_step = 0
    
    while q:
        coords, step = q.pop(0)
        if coords in visited:
            continue
        
        if step != last_step:
            last_step = step
            if (step-1) % 2 == starting_parity:
                step_map[step-1] = len(visited)
            
        if step % 2 == starting_parity:
            visited.add(coords)
        
        possible_moves = [(coords[0]+x[0], coords[1]+x[1]) for x in cardinal_moves]
        filtered_moves = [x for x in possible_moves if x[0] >= 0 and x[1] >= 0 and x[0] < row_count and x[1] < col_count and data[x[0]][x[1]] != '#']
        [q.append([x, step+1]) for x in filtered_moves]
    return step_map

step_max = 100001
c = map_steps_to_locations(s_coords, step_max % 2)
n = map_steps_to_locations((0, col_count // 2), 0)
e = map_steps_to_locations((row_count // 2, col_count - 1), 0)
s = map_steps_to_locations((row_count - 1, col_count // 2), 0)
w = map_steps_to_locations((row_count // 2, 0), 0)
n2 = map_steps_to_locations((0, col_count // 2), 1)
e2 = map_steps_to_locations((row_count // 2, col_count - 1), 1)
s2 = map_steps_to_locations((row_count - 1, col_count // 2), 1)
w2 = map_steps_to_locations((row_count // 2, 0), 1)
ne = map_steps_to_locations((0, col_count - 1), 0)
se = map_steps_to_locations((row_count - 1, col_count - 1), 0)
sw = map_steps_to_locations((row_count - 1, 0), 0)
nw = map_steps_to_locations((0, 0), 0)
ne2 = map_steps_to_locations((0, col_count - 1), 1)
se2 = map_steps_to_locations((row_count - 1, col_count - 1), 1)
sw2 = map_steps_to_locations((row_count - 1, 0), 1)
nw2 = map_steps_to_locations((0, 0), 1)

def evaluate_center(steps):
    max_step = max(c)
    return c[max_step] if steps > max_step else c[steps]
def evaluate(card_1, card_2, inter_1, inter_2, steps):
    side_values = []
    temp_steps = steps - 1 - col_count // 2
    col = steps % 2
    while temp_steps >= 0:
        true_inter = inter_1 if col % 2 == 0 else inter_2
        inter_max_step = max(true_inter)
        side_values.append(true_inter[temp_steps] if temp_steps <= inter_max_step else true_inter[inter_max_step])
        temp_steps -= col_count
        col += 1
    side_sum = sum(side_values)
    
    track = 0
    while steps >= 0:
        row = steps % 2
        true_card = card_1 if row % 2 == 0 else card_2
        max_step = max(true_card)
        track += (true_card[steps] if steps <= max_step else true_card[max_step]) + side_sum
        if len(side_values) != 0:
            side_sum -= side_values.pop(0)
        steps -= row_count
    
    return track

start_steps = step_max - 1 - row_count // 2
ans = 0

ans += evaluate_center(step_max)
ans += evaluate(s, s2, se, se2, start_steps)
ans += evaluate(w, w2, sw, sw2, start_steps)
ans += evaluate(n, n2, nw, nw2, start_steps)
ans += evaluate(e, e2, ne, ne2, start_steps)
print(ans)











