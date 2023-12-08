data = open('Input.txt', 'r').read().split('\n')

instructions = data[0]

dict = {}
for map in data[2::1]:
    equals_split = map.replace(' ', '').replace('(', '').replace(')', '').split('=')
    dict[equals_split[0]] = equals_split[1].split(',')

current_node = 'AAA'
step = 0
while current_node != 'ZZZ':
    direction = instructions[step % len(instructions)]
    step += 1
    current_node = dict[current_node][0 if direction == 'L' else 1]

print(step)