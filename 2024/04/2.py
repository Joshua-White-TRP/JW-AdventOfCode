data = open('Input.txt', 'r').read().split('\n')
d = [[x for x in y] for y in data]
width = len(d[0])
height = len(d)
ans = 0
m_s_arr = ['M','S']

for x in range(width):
    for y in range(height):
        if d[x][y] == 'A' and not (x + 1 >= width or x - 1 < 0 or y + 1 >= height or y - 1 < 0):
            diag_a = d[x+1][y-1] + d[x-1][y+1]
            diag_b = d[x-1][y-1] + d[x+1][y+1]
            
            ans += int(all(s in diag_a and s in diag_b for s in m_s_arr))

print(ans)