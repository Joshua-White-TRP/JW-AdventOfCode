data = open('Input.txt', 'r').read().split('\n')

bricks = []
for line in data:
    start, end = [[int(y) for y in x.split(',')] for x in line.split('~')]
    bricks.append([start, end])
bricks = sorted(bricks, key=lambda x: x[0][2])

#[print(brick) for brick in bricks]
def is_overlap(start1, end1, start2, end2):
    return not (end1 < start2 or end2 < start1)

fallen_bricks = []
for brick in bricks:
    x1, y1, z1 = brick[0]
    x2, y2, z2 = brick[1]
    #print(len(fallen_bricks))
    
    if x1 != x2:
        comparison_bricks = [b for b in fallen_bricks if is_overlap(b[0][0], b[1][0], x1, x2)]
        while z1 > 0 and not any([is_overlap(y1, y2, b[0][1], b[1][1]) and is_overlap(z1-1, z1-1, b[0][2], b[1][2]) for b in comparison_bricks]):
            z1 -= 1
            z2 -= 1
    elif y1 != y2:
        comparison_bricks = [b for b in fallen_bricks if is_overlap(b[0][1], b[1][1], y1, y2)]
        while z1 > 0 and not any([is_overlap(x1, x2, b[0][0], b[1][0]) and is_overlap(z1-1, z1-1, b[0][2], b[1][2]) for b in comparison_bricks]):
            z1 -= 1
            z2 -= 1
    else:
        while z1 > 0 and not any ([is_overlap(x1, x2, b[0][0], b[1][0]) and is_overlap(y1, y2, b[0][1], b[1][1]) for b in fallen_bricks if is_overlap(z1-1, z1-1, b[0][2], b[1][2])]):
            z1 -= 1
            z2 -= 1
    
    fallen_bricks.append([[x1,y1,z1],[x2,y2,z2]])

support_map = {}
for idx, b in enumerate(fallen_bricks):
    bricks_on_top = [idx2 for idx2, b2 in enumerate(fallen_bricks) if b[1][2] + 1 == b2[0][2] and is_overlap(b[0][0], b[1][0], b2[0][0], b2[1][0]) and is_overlap(b[0][1], b[1][1], b2[0][1], b2[1][1])]
    support_map[idx] = bricks_on_top

inverse_support_map = {}
for support in support_map:
    for brick in support_map[support]:
        if brick not in inverse_support_map:
            inverse_support_map[brick] = []
        inverse_support_map[brick].append(support)

ans = 0
for support in support_map:
    ans += all([len(inverse_support_map[x]) > 1 for x in support_map[support]])

#[print(str(x) + ': ' + str(inverse_support_map[x])) for x in inverse_support_map]
[print(str(x) + ': ' + str(support_map[x])) for x in support_map]
print(ans)