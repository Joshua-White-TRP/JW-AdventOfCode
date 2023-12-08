instructions = open('Input.txt', 'r').read().split('\n')

lights_array = [[0] * 1000 for i in range(1000)]

for instruction in instructions:
    type = 0 if 'turn off' in instruction else 1 if 'turn on' in instruction else 2
    
    value_pairs = [''.join([y for y in x if y.isnumeric() or y == ',']).split(',') for x in instruction.split('through')]
    x_range = range(int(value_pairs[0][0]), int(value_pairs[1][0]) + 1)
    y_range = range(int(value_pairs[0][1]), int(value_pairs[1][1]) + 1)
    
    for x in x_range:
        for y in y_range:
            lights_array[x][y] = 1 if type == 1 else (1 if lights_array[x][y] == 0 else 0) if type == 2 else 0

on_count = 0
for x in lights_array:
    for y in x:
        on_count += y

print(on_count)