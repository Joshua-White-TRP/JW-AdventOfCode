data = open('Input.txt', 'r').read().split('\n')
registers = [int(x.split(': ')[1]) for x in data[0:3]]
programs = [int(x) for x in data[4].split(': ')[1].split(',')]

instruction_index = 0
output = []
while instruction_index < len(programs):
    opcode, literal = programs[instruction_index], programs[instruction_index + 1]
    combo = registers[literal - 4] if literal >= 4 and literal <= 6 else literal
    
    if opcode == 0: 
        registers[0] = int(registers[0] / 2**combo)
    elif opcode == 1:
        registers[1] = registers[1] ^ literal
    elif opcode == 2:
        registers[1] = combo % 8
    elif opcode == 3 and registers[0] != 0:
        instruction_index = literal
        continue
    elif opcode == 4:
        registers[1] = registers[1] ^ registers[2]
    elif opcode == 5:
        output.append(combo % 8)
    elif opcode == 6:
        registers[1] = int(registers[0] / 2**combo)
    elif opcode == 7:
        registers[2] = int(registers[0] / 2**combo)
    instruction_index += 2
print(','.join([str(x) for x in output]))