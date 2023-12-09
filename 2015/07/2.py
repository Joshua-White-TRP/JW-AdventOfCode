data = open('Input.txt', 'r').read().split('\n')
dict = {}

def run_instructions(dict, instructions):
    ops = ['AND', 'OR', 'LSHIFT', 'RSHIFT', 'NOT']

    instruction_index = -1
    while len(instructions) != 0:
        instruction_index = 0 if instruction_index + 1 == len(instructions) else instruction_index + 1
        
        split_instruction = instructions[instruction_index].split('->')
        output = split_instruction[1][1::1]
        split_input = split_instruction[0][0:len(split_instruction[0])-1:1].split(' ')
        input_keys = [x for x in split_input if not x.isnumeric() and x not in ops]
        
        if len([input_key for input_key in input_keys if input_key not in dict]) > 0:
            continue
        
        if output not in dict:
            if len(split_input) == 2:
                dict[output] = 65535 - dict[split_input[1]]
            else:
                left_input = int(split_input[0]) if split_input[0].isnumeric() else dict[split_input[0]]
                if len(split_input) == 1:
                    dict[output] = left_input
                else:
                    right_input = int(split_input[2]) if split_input[2].isnumeric() else dict[split_input[2]]
                    
                    if ops[0] in split_input:
                        dict[output] = left_input & right_input
                    elif ops[1] in split_input:
                        dict[output] = left_input | right_input
                    elif ops[2] in split_input:
                        dict[output] = left_input << right_input
                    elif ops[3] in split_input:
                        dict[output] = left_input >> right_input
        
        del instructions[instruction_index]
        instruction_index -= 1

run_instructions(dict, [x for x in data])
dict = {'b': dict['a']}
run_instructions(dict, [x for x in data])

print(dict['a'])