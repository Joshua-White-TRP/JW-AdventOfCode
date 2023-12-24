data = [[y for y in x] for x in open('Input.txt', 'r').read().split('\n')]
dirs = [(-1,0),(0,1),(1,0),(0,-1)]  #nesw
slopes = ['^','>','v','<']

row_count = len(data)
col_count = len(data[0])
start_loc = (0, 1)
end_loc = (row_count - 1, col_count - 2)

def loc_oob(loc, row_count, col_count):
    return loc[0] < 0 or loc[1] < 0 or loc[0] >= row_count or loc[1] >= col_count

split_locs = set()
split_locs.add(start_loc)

for i in range(1, row_count):
    for j in range(1, col_count-1):
        if data[i][j] == '#':
            continue
        
        p_loc = (i, j)
        valid_surrounding_locs = [x for x in [(p_loc[0]+d[0], p_loc[1]+d[1]) for d in dirs] if not loc_oob(x, row_count, col_count) and data[x[0]][x[1]] != '#']
        
        if len(valid_surrounding_locs) > 2:
            split_locs.add(p_loc)

split_loc_maps = {}
for loc in split_locs:
    split_loc_map = {}
    paths = [[set(), loc]]
    paths[0][0].add(loc)

    while paths:
        new_paths = []
        for path, p_loc in paths:
            char = data[p_loc[0]][p_loc[1]]
            next_locs = [(p_loc[0]+d[0], p_loc[1]+d[1]) for idx, d in enumerate(dirs)]
            
            for nl in next_locs:
                if loc_oob(loc, row_count, col_count) or nl in path:
                    continue
                
                nchar = data[nl[0]][nl[1]]
                if nchar == '#':
                    continue
                
                if nl in split_locs or nl == end_loc:
                    split_loc_map[nl] = len(path)
                    continue
                
                new_path = path.copy()
                new_path.add(nl)
                new_paths.append([new_path, nl])
        paths = new_paths
    split_loc_maps[loc] = split_loc_map

ans = 0
paths = [[set(), start_loc, 0]]
paths[0][0].add(start_loc)
while paths:
    new_paths = []
    for path, p_loc, total in paths:
        split_loc_map = split_loc_maps[p_loc]
        
        for node in split_loc_map:
            if node in path:
                continue
            
            new_distance = total + split_loc_map[node]
            if node == end_loc:
                if ans < new_distance:
                    ans = new_distance 
                continue
            
            new_path = path.copy()
            new_path.add(node)
            new_paths.append([new_path, node, new_distance])
            
    paths = new_paths

print(ans)