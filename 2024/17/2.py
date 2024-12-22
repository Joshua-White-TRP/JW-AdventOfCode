data = open('Input.txt', 'r').read().split('\n')
initial_registers = [int(x.split(': ')[1]) for x in data[0:3]]
programs = [int(x) for x in data[4].split(': ')[1].split(',')]

a_value = -1
output = []
while output != programs:
    a_value += 1
    instruction_index = 0
    registers = [x for x in initial_registers]
    registers[0] = a_value
    output = []
    
    if a_value % 100000 == 0:
        print(a_value)
    
    while instruction_index < len(programs):
        opcode, literal = programs[instruction_index], programs[instruction_index + 1]
        combo = registers[literal - 4] if literal >= 4 and literal <= 6 else literal
        new_output_value = combo % 8
        
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
        elif opcode == 5 and len(output) < len(programs) and new_output_value == programs[len(output)]:
            output.append(combo % 8)
        elif opcode == 5:
            break
        elif opcode == 6:
            registers[1] = int(registers[0] / 2**combo)
        elif opcode == 7:
            registers[2] = int(registers[0] / 2**combo)
        instruction_index += 2
#print(','.join([str(x) for x in output]))
print(a_value)