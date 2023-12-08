directions = open('Input.txt', 'r').read()

coords = [[0, 0], [0, 0]]
index_pairs = []

for idx, direction in enumerate(directions):
    coords_index = idx % 2
    index_pairs.append((coords[coords_index][0], coords[coords_index][1]))
    
    if direction == '^':
        coords[coords_index][1] += 1
    elif direction == '>':
        coords[coords_index][0] += 1
    elif direction == 'v':
        coords[coords_index][1] -= 1
    elif direction == '<':
        coords[coords_index][0] -= 1
        
    index_pairs.append((coords[coords_index][0], coords[coords_index][1]))
    

print(len(set(index_pairs)))