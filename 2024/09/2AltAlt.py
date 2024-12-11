data = [int(x) for x in open('Input.txt', 'r').read().split('\n')[0]]

map = []
for i, x in enumerate(data):
    if x != 0:
        if i % 2 == 0:
            map.append([int(i / 2), x])
        else:
            map.append([None, x])

tracker = 0
ans = 0
max_end_tracker = len(map) - 1
for idx, [v, l] in enumerate(map):
    if v == None:
        end_tracker = max_end_tracker
        max_set = False
        while l > 0 and end_tracker > idx:
            ev, el = map[end_tracker]
            if ev != None:
                if not max_set:
                    max_set = True
                    max_end_tracker = end_tracker
                
                if el <= l:
                    for y in range(el):
                        ans += tracker * ev
                        tracker += 1
                    map[end_tracker][0] = None
                    l -= el
            end_tracker -= 1
        tracker += l
    else:
        for y in range(l):
            ans += tracker * v
            tracker += 1

print(ans)