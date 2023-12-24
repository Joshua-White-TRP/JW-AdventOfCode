data = [[y for y in x] for x in open('Input.txt', 'r').read().split('\n')]
dirs = [(-1,0),(0,1),(1,0),(0,-1)]  #nesw
slopes = ['^','>','v','<']

row_count = len(data)
col_count = len(data[0])

def loc_oob(loc, row_count, col_count):
    return loc[0] < 0 or loc[1] < 0 or loc[0] >= row_count or loc[1] >= col_count

loc = (0,1)
paths = [[set(), loc]]
paths[0][0].add(loc)
ans = 0

while paths:
    new_paths = []
    for path, p_loc in paths:
        char = data[p_loc[0]][p_loc[1]]
        next_locs = [(p_loc[0]+d[0], p_loc[1]+d[1]) for idx, d in enumerate(dirs) if (char not in slopes or char == slopes[idx])]
        
        for nl in next_locs:
            if loc_oob(loc, row_count, col_count) or nl in path:
                continue
            
            nchar = data[nl[0]][nl[1]]
            if nl[0] == row_count - 1 and nchar == '.':
                if len(path) > ans:
                    ans = len(path)
                continue
            
            if nchar == '#':
                continue
            
            new_path = path.copy()
            new_path.add(nl)
            new_paths.append([new_path, nl])
    paths = new_paths

print(ans)