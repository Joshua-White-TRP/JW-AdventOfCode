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
        
        perimeter = 4
        for d in ds:
            to_check = [loc for loc in current_coords if [loc[0]+d[0],loc[1]+d[1]] not in current_coords]
            movement_index = d.index(0)
            stationary_index = int(not movement_index)
            to_check.sort(key=lambda x: (x[stationary_index], x[movement_index]))
            
            last_value = None
            for x in to_check:
                if last_value != None and (x[stationary_index] != last_value[stationary_index] or x[movement_index] != last_value[movement_index] + 1):
                    perimeter += 1
                last_value = x
        
        ans += len(current_coords) * perimeter

print(ans)