data = open('InputAlt.txt', 'r').read().split('\n')
bits = {}
instructions = []

after_blank = False
for x in data:
    if x == '':
        after_blank = True
    elif after_blank:
        instructions.append(x.split(' '))
    else:
        split = x.split(': ')
        bits[split[0]] = int(split[1])

while len(instructions) > 0:
    new_instructions = []
    for ins in instructions:
        a, o, b, arrow, c = ins
        if a not in bits or b not in bits:
            new_instructions.append(ins)
            continue
         
        a, b = bits[a], bits[b]
        bits[ins[4]] = int(a and b) if o == 'AND' else int(a or b) if o == 'OR' else int((a and not b) or (b and not a))
    instructions = new_instructions

sorted_keys = sorted([x for x in bits if x[0] == 'z'])
print(int(''.join([str(bits[x]) for x in sorted_keys[::-1]]), 2))