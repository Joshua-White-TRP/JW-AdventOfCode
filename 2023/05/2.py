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
    
seed_minimums = []
seed_maximums = []
for idx, seed in enumerate(seeds):
    if idx % 2 == 0:
        seed_minimums.append(seed)
    else:
        seed_maximums.append(seed_minimums[len(seed_minimums) - 1] + seed - 1)

def getMinimumMap(seed_minimum, seed_maximum, maps_v2, map_v2_index):
    map_v2 = maps_v2[map_v2_index]
    recursion_answers = []
    
    for set in map_v2:
        setMinimum = set[0]
        setMaximum = set[1]
        minimum_is_in_range = seed_minimum >= setMinimum and seed_minimum <= setMaximum
        maximum_is_in_range = seed_maximum <= setMaximum and seed_maximum >= setMinimum
        
        if not minimum_is_in_range and not maximum_is_in_range and not (seed_minimum <= setMinimum and seed_maximum >= setMaximum):
            continue
        
        new_range_minimum = (seed_minimum if minimum_is_in_range else setMinimum) + set[2]
        new_range_maximum = (seed_maximum if maximum_is_in_range else setMaximum) + set[2]
        
        if(map_v2_index + 1 == len(maps_v2)):
            recursion_answers.append(new_range_minimum)
        else:
            recursionAnswer = getMinimumMap(new_range_minimum, new_range_maximum, maps_v2, map_v2_index + 1)
            if recursionAnswer != None:
                recursion_answers.append(recursionAnswer)
    
    recursion_answers.sort()
    if len(recursion_answers) == 0:
        return None
        
    return recursion_answers[0]

location_minimums = []
for idx, seed_minimum in enumerate(seed_minimums):
    newAns = getMinimumMap(seed_minimum, seed_maximums[idx], maps_v2, 0)
    if newAns != None:
        location_minimums.append(newAns)
    
location_minimums.sort()
print(location_minimums)
print(location_minimums[0])