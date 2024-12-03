import re
import math

data = open('Input.txt', 'r').read()
enabled = True
ans = 0

for v in re.findall("mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", data):
    if v == "do()":
        enabled = True
    elif v == "don't()":
        enabled = False
    elif enabled:
        ans += math.prod([int(x) for x in v[v.index("(")+1:-1].split(",")])

print(ans)