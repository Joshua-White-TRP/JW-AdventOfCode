data = [[int(y) for y in x] for x in open('Input.txt', 'r').read().split('\n')]
ds = [[-1,0],[0,1],[1,0],[0,-1]]
ans = 0

def search(data, p):
    values = []
    p_num = data[p[0]][p[1]]
    for d in ds:
        loc = [p[0] + d[0], p[1] + d[1]]
        if is_in_range(data, loc[0], loc[1]) and data[loc[0]][loc[1]] == p_num + 1:
            if p_num == 8:
                values.append(loc)
            else:
                values.extend(search(data, loc))
    
    return values
    
def is_in_range(data, y, x):
    return x >= 0 and y >= 0 and y < len(data) and x < len(data[0])

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == 0:
            nines = search(data, [y,x])
            ans += len([(n[0],n[1]) for n in nines if n != None])

print(ans)