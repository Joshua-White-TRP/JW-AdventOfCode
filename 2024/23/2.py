from itertools import combinations
data = open('Input.txt', 'r').read().split('\n')

node_map = {}
for d in data:
    links = [d.split('-')]
    links.append(links[0][::-1])
    
    for c in links:
        s, e = c
        if s not in node_map:
            node_map[s] = set()
            node_map[s].add(s)
        node_map[s].add(e)

groupings = set()
grouping_size = 2
while len(groupings) != 1:
    groupings = set()
    for n in [n for n in node_map if n[0] == 't']:
        for p in [tuple(sorted(p)) for p in combinations(node_map[n], grouping_size) if n in p]:
            other_nodes = [x for x in p if x != n]
            if all([all([o in node_map[o2] for o2 in other_nodes if o2 != o]) for o in other_nodes]):
                groupings.add(p)
    print(str(grouping_size) + ': ' + str(len(groupings)))
    grouping_size += 1
print(','.join(sorted(list(groupings)[0])))