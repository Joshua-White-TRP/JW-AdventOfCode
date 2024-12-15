data = open('Input.txt', 'r').read().split('\n')
splits = [[y.split('=')[1].split(',') for y in x] for x in [x.split(' ') for x in data]]
splits = [[[int(z) for z in y] for y in x] for x in splits]
output_file = 'Output.txt'

open(output_file, "w")
width, height = 100, 102
hw, hh = (width + 1) / 2, (height + 1) / 2
final_positions = []

#After initially testing the output I noticed a consistent cluster every 101 steps for my test data.
#Working back, this gives a starting number of steps of 68 and after checking the output every 101 steps
#a tree is made!
skip = 68
tracker = 0
while tracker <= 10000:
    tracker += skip
    final_positions = []
    for split in splits:
        p, v = split
        p[0], p[1] = (p[0] + v[0] * skip) % (width + 1), (p[1] + v[1] * skip) % (height + 1)
        
        final_positions.append([p[0], p[1]])

    with open(output_file, "a") as f:
        for i in range(height + 1):
            row = []
            for j in range(width + 1):
                num = final_positions.count([j,i])
                row.append(' ' if num == 0 else str(num))
            f.write(''.join(row) + '\n')
    
        f.write(str(tracker) + '\n')
        f.write('-------\n')
    print(tracker)
    skip = 101