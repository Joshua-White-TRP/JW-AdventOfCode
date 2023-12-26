data = open('Input.txt', 'r').read().split('\n')

full_mapping = {}
for line in data:
    a, b = line.split(': ')
    b = b.split(' ')
    
    full_mapping[a] = (full_mapping[a] if a in full_mapping else []) + b
    for c in b:
        full_mapping[c] = (full_mapping[c] if c in full_mapping else []) + [a]

unprocessed = dict([(x, 0) for x in full_mapping])
processed = []

while unprocessed and sum([unprocessed[x] for x in unprocessed]) != 3:
    max_ans = -1
    for u in unprocessed:
        if unprocessed[u] > max_ans:
            max_ans = unprocessed[u]
            max_u = u
    
    for connection in [x for x in full_mapping[max_u] if x in unprocessed]:
        unprocessed[connection] += 1
    
    processed.append(max_u)
    del unprocessed[max_u]

print(len(processed) * len(unprocessed))