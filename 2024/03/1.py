import re
import math

data = open('Input.txt', 'r').read()
ans = 0

for mul in re.findall("mul\([0-9]+,[0-9]+\)", data):
    ans += math.prod([int(x) for x in mul[mul.index("(")+1:-1].split(",")])

print(ans)