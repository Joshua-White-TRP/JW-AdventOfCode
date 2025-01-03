data = open('Input.txt', 'r').read().split('\n')
splits = [[int(y) for y in x.split(' ')] for x in data]
ans = 0

for split in splits:
    for x in [split, *[[y for idx_y, y in enumerate(split) if idx_y != idx_x] for idx_x, x in enumerate(split)]]:
        is_ascending = None
        prev_num = x[0]
        safe = True
        
        for y in x[1:]:
            cur_num = y
            diff = abs(cur_num - prev_num)
            
            if (is_ascending != None and is_ascending != (cur_num > prev_num)) or diff < 1 or diff > 3:
                safe = False
                break
                
            is_ascending = cur_num > prev_num
            prev_num = cur_num
        
        if safe:
            ans += 1
            break

print(ans)