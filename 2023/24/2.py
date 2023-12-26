from math import ceil, floor
data = open('Input.txt', 'r').read().split('\n')

hailstones = []
for line in data:
    hailstones.append([[int(y) for y in x.split(', ')] for x in line.split(' @ ')])

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

m = 400000000000000

for x in range(-500, 500):
    print(x)
    for y in range(-500, 500):
        t_v = [x,y,0]
        a = [*hailstones[0][0], *[x - t_v[idx] for idx, x in enumerate(hailstones[0][1])]]
        b = [*hailstones[1][0], *[x - t_v[idx] for idx, x in enumerate(hailstones[1][1])]]
        
        xy = line_intersection([(a[0], a[1]), (a[0] + a[3] * m , a[1] + a[4] * m)], [(b[0], b[1]), (b[0] + b[3] * m, b[1] + b[4] * m)])
        if xy == None:
            continue
        ix, iy = xy
        if ix % 1 != 0 or iy % 1 != 0:
            continue
        
        for z in range(-500, 500):
            a[5] -= z
            b[5] -= z
            xz = line_intersection([(a[0], a[2]), (a[0] + a[3] * m , a[2] + a[5] * m)], [(b[0], b[2]), (b[0] + b[3] * m, b[2] + b[5] * m)])
            yz = line_intersection([(a[1], a[2]), (a[1] + a[4] * m , a[2] + a[5] * m)], [(b[1], b[2]), (b[1] + b[4] * m, b[2] + b[5] * m)])
            a[5] += z
            b[5] += z
            
            if xz == None or yz == None:
                continue
            ix2, iz = xz
            iy2, iz2 = yz
            if iz % 1 != 0 or ix != ix2 or iy != iy2 or iz != iz2:
                continue

            t_v2 = [x,y,z]
            all_valid = True
            for hailstone in hailstones[2:]:
                px, py, pz = hailstone[0]
                vx, vy, vz = [hv - t_v2[idx] for idx, hv in enumerate(hailstone[1])]
                
                if vx == 0 or vy == 0 or vz == 0 or (px - ix) / vx % 1 != 0 or (py - iy) / vy % 1 != 0 or (pz - iz) / vz % 1 != 0:
                    all_valid = False
                    break
                
            if all_valid:
                print(ix, iy, iz)
                print(t_v2)
                print(int(ix + iy + iz))
                exit()
