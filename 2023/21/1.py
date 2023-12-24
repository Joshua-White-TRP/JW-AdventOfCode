data = [[y for y in x] for x in open('Input.txt', 'r').read().split('\n')]
cardinal_moves = [(-1,0),(0,1),(1,0),(0,-1)]

row_count = len(data)
col_count = len(data)
s_coords = (row_count//2, col_count//2)

visited = set()
q = [[s_coords, 0]]
while q:
    coords, step = q.pop(0)
    if step > 64 or coords in visited:
        continue
    if step % 2 == 0:
        visited.add(coords)
    
    possible_moves = [(coords[0]+x[0], coords[1]+x[1]) for x in cardinal_moves]
    filtered_moves = [x for x in possible_moves if x[0] >= 0 and x[1] >= 0 and x[0] < row_count and x[1] < col_count and data[x[0]][x[1]] != '#']
    
    [q.append([x, step+1]) for x in filtered_moves]
print(len(visited))