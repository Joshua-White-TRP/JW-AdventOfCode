data = open('Input.txt', 'r').read().split('\n')

galaxy_locations = []
empty_row_indexes = [True] * len(data)
empty_column_indexes = [True] * len(data)

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == '#':
            galaxy_locations.append([i,j])
            empty_row_indexes[i] = False
            empty_column_indexes[j] = False

empty_row_indexes = [idx for idx, x in enumerate(empty_row_indexes) if x]
empty_column_indexes = [idx for idx, x in enumerate(empty_column_indexes) if x]
additional_distance = 999999
answer = 0

for i in range(len(galaxy_locations)):
    a = galaxy_locations[i]
    for j in range(i+1, len(galaxy_locations)):
        b = galaxy_locations[j]
        
        x_range = range(a[0], b[0])
        y_range = range(a[1], b[1]) if a[1] <= b[1] else range(b[1], a[1])
        
        x_diff = b[0] - a[0]
        y_diff = abs(b[1] - a[1])
        x_gap_distance = len([x for x in x_range if x in empty_row_indexes]) * additional_distance
        y_gap_distance = len([y for y in y_range if y in empty_column_indexes]) * additional_distance
        
        answer += x_diff + y_diff + x_gap_distance + y_gap_distance

print(answer)