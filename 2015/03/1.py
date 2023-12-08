directions = open('Input.txt', 'r').read()

x_index = 0
y_index = 0
index_pairs = []

for direction in directions:
    index_pairs.append((x_index, y_index))
    
    if direction == '^':
        y_index += 1
    elif direction == '>':
        x_index += 1
    elif direction == 'v':
        y_index -= 1
    elif direction == '<':
        x_index -= 1
    
    index_pairs.append((x_index, y_index))

print(len(set(index_pairs)))