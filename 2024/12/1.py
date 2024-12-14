data = open('Input.txt', 'r').read().split('\n')
ds = [[-1,0],[0,1],[1,0],[0,-1]]
visited_locations = []
ans = 0

def is_in_range(data, y, x):
    return x >= 0 and y >= 0 and y < len(data) and x < len(data[0])
def search(data, letter, y, x):
    if is_in_range(data, y, x) and [y,x] not in visited_locations and data[y][x] == letter:
        visited_locations.append([y,x])
        searches = [search(data, letter, y + d[0], x + d[1]) for d in ds]
        
        ret = [[y,x]]
        ret.extend([c for v in searches if v != None for c in v])
        return ret
    return None

for y in range(len(data)):
    for x in range(len(data[0])):
        if [y,x] in visited_locations:
            continue
        
        letter = data[y][x]
        current_coords = search(data, letter, y, x)
        
        perimeter = 0
        for loc in current_coords:
            for d in ds:
                edge = [loc[0] + d[0], loc[1] + d[1]]
                perimeter += int(not is_in_range(data, edge[0], edge[1]) or edge not in current_coords)
        ans += len(current_coords) * perimeter

print(ans)