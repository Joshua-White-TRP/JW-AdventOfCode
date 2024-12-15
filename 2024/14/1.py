import math
data = open('Input.txt', 'r').read().split('\n')
splits = [[y.split('=')[1].split(',') for y in x] for x in [x.split(' ') for x in data]]
splits = [[[int(z) for z in y] for y in x] for x in splits]

width, height = 100, 102
hw, hh = (width + 1) / 2, (height + 1) / 2

w_left, w_right = [0,math.floor(hw)-1], [math.ceil(hw),width]
h_top, h_bottom = [0,math.floor(hh)-1], [math.ceil(hh),height]
quad_ranges = [[w_left,h_top],[w_right,h_top],[w_left,h_bottom],[w_right,h_bottom]]
quad_sums = [0,0,0,0]

for split in splits:
    p, v = split
    p_x, p_y = (p[0] + v[0] * 100) % (width + 1), (p[1] + v[1] * 100) % (height + 1)
    
    for idx, quad_range in enumerate(quad_ranges):
        if quad_range[0][1] >= p_x >= quad_range[0][0] and quad_range[1][1] >= p_y >= quad_range[1][0]:
            quad_sums[idx] += 1
            break

print(quad_sums)
print(math.prod(quad_sums))