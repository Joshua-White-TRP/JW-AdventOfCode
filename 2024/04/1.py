data = open('Input.txt', 'r').read().split('\n')
d = [[x for x in y] for y in data]
width = len(d[0])
height = len(d)
ans = 0
t = 'MAS'

def search(sx, sy, x_inc, y_inc):
    return int(
        width > sx + (x_inc * 3) >= 0 and
        height > sy + (y_inc * 3) >= 0 and
        d[sx + x_inc][sy + y_inc] + d[sx + x_inc * 2][sy + y_inc * 2] + d[sx + x_inc * 3][sy + y_inc * 3] == t
    )

for x in range(width):
    for y in range(height):
        if d[x][y] == 'X':
            ans += (
                search(x,y,1,0) + search(x,y,-1,0) + search(x,y,0,1) + search(x,y,0,-1) +
                search(x,y,1,1) + search(x,y,-1,1) + search(x,y,1,-1) + search(x,y,-1,-1)
            )

print(ans)