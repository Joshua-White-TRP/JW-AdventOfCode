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

triplets = set()
for n in [n for n in node_map if n[0] == 't']:
    combos = combinations(node_map[n], 3)
    nodes_to_check = [tuple(sorted(p)) for p in combos if n in p]
    
    for p in nodes_to_check:
        other_nodes = [x for x in p if x != n]
        if other_nodes[1] in node_map[other_nodes[0]] and other_nodes[0] in node_map[other_nodes[1]]:
            triplets.add(p)
print(len(triplets))