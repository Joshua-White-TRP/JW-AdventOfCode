data = open('Input.txt', 'r').read().split('\n')
ds = [[-1,0],[0,1],[1,0],[0,-1]]

start, end = None, None
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == 'S':
            start = (y,x)
        elif data[y][x] == 'E':
            end = (y,x)
    if start != None and end != None:
        break

path, tracker = [start], start
while tracker != end:
    y, x = tracker
    for d in ds:
        ny, nx = y+d[0], x+d[1]
        if data[ny][nx] != '#' and (ny, nx) not in path:
            break
    
    tracker = (ny, nx)
    path.append(tracker)

ans = 0
successes = []
for idx, node in enumerate(path[:len(path)-102]):
    for d in ds:
        for node2 in path[idx+102:]:
            if node2[0] == node[0] + d[0] * 2 and node2[1] == node[1] + d[1] * 2:
                ans += 1
                successes.append([node, node2])
[print(str(x) + ':   ' + str(abs(x[0][0] - x[1][0]) + abs(x[0][1] - x[1][1]))) for x in successes]
print(ans)