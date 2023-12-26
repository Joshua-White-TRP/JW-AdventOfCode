data = open('Input.txt', 'r').read().split('\n')

hailstones = []
for line in data:
    hailstones.append([[int(y) for y in x.split(', ')] for x in line.split(' @ ')])

h_count = len(hailstones)
min = 200000000000000
max = 400000000000000

hailstone_coords = []
for hailstone in hailstones:
    a_p, a_v = hailstone
    
    a_s = a_p.copy()
    a_e = a_p.copy()
    
    a_s_x_dif = (min - a_p[0]) / a_v[0]
    a_s_y_dif = (min - a_p[1]) / a_v[1]
    a_e_x_dif = (max - a_p[0]) / a_v[0]
    a_e_y_dif = (max - a_p[1]) / a_v[1]
    
    a_s_dif = a_s_x_dif if abs(a_s_x_dif) <= abs(a_s_y_dif) else a_s_y_dif
    a_e_dif = a_e_x_dif if abs(a_e_x_dif) <= abs(a_e_y_dif) else a_e_y_dif
    
    a_s[0] = a_s[0] + a_v[0] * a_s_dif
    a_s[1] = a_s[1] + a_v[1] * a_s_dif
    a_e[0] = a_e[0] + a_v[0] * a_e_dif
    a_e[1] = a_e[1] + a_v[1] * a_e_dif
    
    hailstone_coords.append((a_s, a_e))

def det(a, b):
    return a[0] * b[1] - a[1] * b[0]

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    div = det(xdiff, ydiff)
    if div == 0:
        return None

    d = (det(*line1), det(*line2))
    return det(d, xdiff) / div, det(d, ydiff) / div

ans = 0
for i in range(h_count):
    for j in range(i + 1, h_count):
        a_s, a_e = hailstone_coords[i]
        b_s, b_e = hailstone_coords[j]
        
        inter = line_intersection((a_s, a_e), (b_s, b_e))
        if inter != None and inter[0] >= min and inter[0] <= max and inter[1] >= min and inter[1] <= max:
            a_h = hailstones[i]
            b_h = hailstones[j]
            
            if (inter[0] >= a_h[0][0] if a_h[1][0] >= 0 else inter[0] <= a_h[0][0]) and (inter[1] >= b_h[0][1] if b_h[1][1] >= 0 else inter[1] <= b_h[0][1]):
                ans += 1
print(ans)