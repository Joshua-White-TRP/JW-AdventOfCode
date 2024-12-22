import sys
sys.setrecursionlimit(10000)

data = [[int(y) for y in x.split(',')] for x in open('Input.txt', 'r').read().split('\n')]
ds = [[-1,0],[0,1],[1,0],[0,-1]]
wh = 71
sim = 1024
print(data[sim])

grid = []
for i in range(wh):
    row = []
    for j in range(wh):
        row.append('.')
    grid.append(row)

for loc in data[:sim]:
    grid[loc[1]][loc[0]] = '#'

end = (wh-1, wh-1)
def is_in_range(data, y, x):
    return x >= 0 and y >= 0 and y < len(data) and x < len(data[0])
def move(p, vis, dsf_idx, score):
    global ans
    global final_path
    
    loc = (p, dsf_idx)
    if (score >= ans or
        (loc in unique_locations and unique_locations[loc] <= score)):
        return
    unique_locations[loc] = score
    
    vis.add(p)
    if p == end:
        if score < ans:
            ans = score
            final_path = vis
        return
    
    dsr_idx, dsl_idx = (dsf_idx+1) % 4, (dsf_idx-1) % 4
    dsf, dsr, dsl = ds[dsf_idx], ds[dsr_idx], ds[dsl_idx]
    f, r, l = (p[0]+dsf[0], p[1]+dsf[1]), (p[0]+dsr[0], p[1]+dsr[1]), (p[0]+dsl[0], p[1]+dsl[1])
    
    if is_in_range(grid, f[0], f[1]) and grid[f[0]][f[1]] != '#' and f not in vis:
        move(f, set(vis), dsf_idx, score + 1)
    if is_in_range(grid, r[0], r[1]) and grid[r[0]][r[1]] != '#' and r not in vis:
        move(r, set(vis), dsr_idx, score + 1)
    if is_in_range(grid, l[0], l[1]) and grid[l[0]][l[1]] != '#' and l not in vis:
        move(l, set(vis), dsl_idx, score + 1)

while True:
    ans = wh*wh*wh
    unique_locations = {}
    final_path = ()
    move((0, 0), set(), 1, 0)
    
    if ans == wh*wh*wh:
        break
    
    print('-------------')
    print(sim)
    print(data[sim])
    grid[data[sim][1]][data[sim][0]] = '#'
    [print(''.join(x)) for x in [[grid[y][x] if (y,x) not in final_path else 'O' for x in range(len(grid[0]))] for y in range(len(grid))]]
    
    sim += 1
