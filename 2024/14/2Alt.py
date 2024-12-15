data = open('Input.txt', 'r').read().split('\n')
splits = [[y.split('=')[1].split(',') for y in x] for x in [x.split(' ') for x in data]]
splits = [[[int(z) for z in y] for y in x] for x in splits]
output_file = 'Output.txt'

open(output_file, "w")
width, height = 100, 102
hw, hh = (width + 1) / 2, (height + 1) / 2
final_positions = []

tracker = 0
while tracker <= 10000:
    tracker += 1
    final_positions = {}
    for split in splits:
        p, v = split
        p[0], p[1] = (p[0] + v[0]) % (width + 1), (p[1] + v[1]) % (height + 1)
        
        if p[1] not in final_positions:
            final_positions[p[1]] = set()
        final_positions[p[1]].add(p[0])

    largest_column = 1 
    for key in final_positions:
        arr = sorted(list(final_positions[key]))
        column_track, prev_v = 1, arr[0]
        for v in arr[1:]:
            if v == prev_v + 1:
                column_track += 1
            else:
                if column_track > largest_column:
                    largest_column = column_track
                column_track = 1
            prev_v = v
    
    if largest_column > 10:
        for i in range(height + 1):
            row = []
            for j in range(width + 1):
                num = 0 if i not in final_positions else int(j in final_positions[i])
                row.append(' ' if num == 0 else str(num))
            print(''.join(row))
        print(tracker)