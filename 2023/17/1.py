from heapq import heappush, heappop
data = [[int(y) for y in x] for x in open('Input.txt', 'r').read().split('\n')]
row_count = len(data)
col_count = len(data[0])
dict_map = {}

for x, row in enumerate(data):
    for y, cell in enumerate(row):
        dict_map[(x, y)] = cell

directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
heap = [(0, (0, 0), 0, 0)]
visited = {((0, 0), 0, 0)}

while len(heap):
    loss, coords, last_direction_index, steps = heappop(heap)
    
    for next_direction_index, direction in enumerate(directions):
        if abs(next_direction_index - last_direction_index) != 1 and next_direction_index != last_direction_index and next_direction_index + last_direction_index != len(directions) - 1:
            continue
        elif next_direction_index == last_direction_index:
            if steps == 3:
                continue
            else:
                steps_in_last_direction = steps + 1
        else:
            steps_in_last_direction = 1
        
        next_coords = coords[0] + directions[next_direction_index][0], coords[1] + directions[next_direction_index][1]
        
        if next_coords in dict_map and (next_coords, next_direction_index, steps_in_last_direction) not in visited:
            next_loss = loss + dict_map[next_coords]
            if next_coords == (row_count - 1, col_count - 1):
                print(next_loss)
                quit()
            
            heappush(heap, (next_loss, next_coords, next_direction_index, steps_in_last_direction))
            visited.add((next_coords, next_direction_index, steps_in_last_direction))