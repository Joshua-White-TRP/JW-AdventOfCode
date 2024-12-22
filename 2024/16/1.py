import sys
sys.setrecursionlimit(10000)

data = open('Input.txt', 'r').read().split('\n')
ds = [[-1,0],[0,1],[1,0],[0,-1]]

t_pos = None
for y in range(1,len(data)-1):
    for x in range(1,len(data[0])-1):
        if data[y][x] == 'S':
            t_pos = (y,x)
            break
    if t_pos != None:
        break
print(t_pos)

ans = 999999999999999
unique_locations = {}
def move(p, vis, dsf_idx, score):
    global ans
    
    loc = (p, dsf_idx)
    if (score > ans or
        (loc in unique_locations and unique_locations[loc] < score)):
        return
    unique_locations[loc] = score
    
    print(len(unique_locations))
    vis.add(p)
    if data[p[0]][p[1]] == 'E':
        if score < ans:
            ans = score
        return
    
    dsr_idx, dsl_idx = (dsf_idx+1) % 4, (dsf_idx-1) % 4
    dsf, dsr, dsl = ds[dsf_idx], ds[dsr_idx], ds[dsl_idx]
    f, r, l = (p[0]+dsf[0], p[1]+dsf[1]), (p[0]+dsr[0], p[1]+dsr[1]), (p[0]+dsl[0], p[1]+dsl[1])
    
    if data[f[0]][f[1]] != '#' and f not in vis:
        move(f, set(vis), dsf_idx, score + 1)
    if data[r[0]][r[1]] != '#' and r not in vis:
        move(r, set(vis), dsr_idx, score + 1001)
    if data[l[0]][l[1]] != '#' and l not in vis:
        move(l, set(vis), dsl_idx, score + 1001)

move(t_pos, set(), 1, 0)
print(ans)