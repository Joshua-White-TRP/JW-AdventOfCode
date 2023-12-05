data = open('Input.txt', 'r').read().split('\n')
seeds = [int(a) for a in data[0][data[0].find(':')+2::1].split(' ')]
maps = []

map_index = -1
for x in data[1::1]:
    if len(x) == 0:
        map_index += 1
        maps.append([])
        continue
    
    if x[0].isnumeric():
        maps[map_index].append([int(a) for a in x.split(' ')])

maps_v2 = []
for map in maps:
    maps_v2.append([])
    map_v2_index = len(maps_v2)-1
    for set in map:
        maps_v2[map_v2_index].append([set[1], set[1] + set[2] - 1, set[0] - set[1]])    #sourceMin, sourceMax, diff

tracked_mappings = [seeds]
mapIndex = 0
while mapIndex < len(maps_v2):
    tracked_mappings_length = len(tracked_mappings)
    last_mappings = tracked_mappings[tracked_mappings_length - 1]
    tracked_mappings.append([])
    
    for mapping in last_mappings:
        detected_match = False
        
        for set in maps_v2[mapIndex]:
            if mapping >= set[0] and mapping <= set[1]:
                detected_match = True
                tracked_mappings[tracked_mappings_length].append(mapping + set[2])
                break
            
        if detected_match == False:
            tracked_mappings[tracked_mappings_length].append(mapping)
    
    mapIndex += 1
    
locations = tracked_mappings[len(tracked_mappings) - 1]
locations.sort()
print(locations[0])