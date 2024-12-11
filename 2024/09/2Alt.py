data = [int(x) for x in open('Input.txt', 'r').read().split('\n')[0]]

map = []
for i, x in enumerate(data):
    if x == 0:
        continue
    
    if i % 2 == 0:
        map.append([int(i / 2), x])
    else:
        map.append([None, x])

end_tracker = len(map) - 1
earliest_none_idx = 0
while end_tracker > 0:
    start_tracker = earliest_none_idx
    earliest_set = False
    file_value, file_length = map[end_tracker]
    
    if file_value != None:
        while start_tracker < end_tracker:
            space_value, space_length = map[start_tracker]
            if space_value == None:
                if not earliest_set:
                    earliest_set = True
                    earliest_none_idx = start_tracker
                
                if space_length >= file_length:
                    map[end_tracker][0] = None
                    map[start_tracker][0] = file_value
                    if space_length > file_length:
                        map[start_tracker][1] = file_length
                        if map[start_tracker + 1][0] == None:
                            map[start_tracker + 1][1] += space_length - file_length
                        else:
                            map.insert(start_tracker + 1, [None, space_length - file_length])
                            end_tracker += 1
                    break
            start_tracker += 1
    end_tracker -= 1

tracker = 0
ans = 0
for x in map:
    for y in range(x[1]):
        if x[0] != None:
            ans += tracker * x[0]
        tracker += 1

print(ans)