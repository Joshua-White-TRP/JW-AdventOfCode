from math import gcd

data = open('Input.txt', 'r').read().split('\n')
instructions = data[0]

dict = {}
for map in data[2::1]:
    equals_split = map.replace(' ', '').replace('(', '').replace(')', '').split('=')
    dict[equals_split[0]] = equals_split[1].split(',')

current_nodes = [x for x in dict.keys() if x[2] == 'A']
steps = []

for current_node in current_nodes:
    step = 0
    
    while current_node[2] != 'Z':
        direction = instructions[step % len(instructions)]
        step += 1
        current_node = dict[current_node][0 if direction == 'L' else 1]
    
    steps.append(step)
    
true_steps = 1
for step in steps:
    true_steps = true_steps * step // gcd(true_steps, step)
print(true_steps)