from itertools import permutations
data = open('Input.txt', 'r').read().split('\n')

def add_to_map(map, start, end, val):
    if not start in map:
        map[start] = {}
    map[start][end] = int(val)
    
location_mappings = {}
for line in data:
    x = line.split(' ')[::2]
    add_to_map(location_mappings, x[0], x[1], x[2])
    add_to_map(location_mappings, x[1], x[0], x[2])

minimum_distance = None
for order in permutations([x for x in location_mappings.keys()]):
    order_total = 0
    for idx, location in enumerate(order[:len(order)-1]):
        order_total += location_mappings[location][order[idx+1]]
    
    if minimum_distance == None or minimum_distance > order_total:
        minimum_distance = order_total

print(minimum_distance)