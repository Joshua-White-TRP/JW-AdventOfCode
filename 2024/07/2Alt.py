import math

data = open('Input.txt', 'r').read().split('\n')
splits = [x.split(': ') for x in data]
ans = 0
for x in splits:
    x[0], x[1] = int(x[0]), [int(v) for v in x[1].split(' ')]

for x in splits:
    ongoing_calcs = [x[1][0]]
    
    for y in x[1][1:]:
        ongoing_calcs = [c for c in list(set(ongoing_calcs)) if c <= x[0]]
        
        for i in range(len(ongoing_calcs)):
            ongoing_calcs.append(ongoing_calcs[i] * y)
            ongoing_calcs.append(int(str(ongoing_calcs[i]) + str(y)))
            ongoing_calcs[i] += y
    
    if any([r == x[0] for r in ongoing_calcs]):
        ans += x[0]

print(ans)