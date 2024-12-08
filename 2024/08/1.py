data = open('Input.txt', 'r').read().split('\n')
dict = {}
h = len(data)
w = len(data[0])
antinodes = set()

for y in range(h):
    for x in range(w):
        v = data[y][x]
        if v != '.':
            if v not in dict:
                dict[v] = []
            dict[v].append([y,x])

def is_in_range(data, y, x):
    return x >= 0 and y >= 0 and y < len(data) and x < len(data[0])

for key in dict:
    antennas = dict[key]
    for a in range(len(antennas)-1):
        for b in range(a+1, len(antennas)):
            ya,xa = antennas[a]
            yb,xb = antennas[b]
            
            y1, x1 = yb + (yb - ya), xb + (xb - xa)
            y2, x2 = ya + (ya - yb), xa + (xa - xb)
            
            if is_in_range(data, y1, x1):
                antinodes.add((y1, x1))
            if is_in_range(data, y2, x2):
                antinodes.add((y2, x2))

print(len(antinodes))