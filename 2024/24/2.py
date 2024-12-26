# One I should revisit in future!
#
# WARNING: This file is definitely not tested for all edge cases, but hopefully handles the ones that will appear in the Input.
# I wasn't satisfied having only a manual workout so wanted to at least try adapt my manual work into a program.
# Between the 2nd and last number a consistent loop of 5 instructions occur (XOR/AND/AND/OR/XOR).
#  In this loop, the:
#   1st instruction (XOR) should use the current x/y values for input.
#   2nd instruction (AND) should use the previous x/y values for input.
#   3rd instruction (AND) should use the outputs of the previous loop's instructions 1 and 4 instruction...
#     UNLESS it's the first loop then use the first XOR + AND instructions used to calculate z01.
#   4th instruction (OR) should use the outputs of instructions 2 and 3.
#   5th instruction (XOR) should use the outputs of instructions 1 and 4...
#     THEN output to z of the same index as the x/y values in instruction 1.
# 
# As my problem only required swaps on invalid OR/XOR instructions these are all I have tested for so far.
#
# Untested theory:
#   Instruction 3 can't be broken without being fixed before reaching it. The 2 inputs used for instruction 3...
#     are already used for instruction 5 in the previous loop, meaning it should be caught early.
#
# Definite problems that could cause problems but hopefully not for the Inputs given for this challenge:
#   If both inputs for instructions 3/4/5 have been swapped for values later in the program.
#   If instructions outside the loop are swapped.
#   Incorrect outputs for the first 2 instructions in each loop (XOR/AND).
#   Incorrect outputs assigned to values before the loop (First 4 instructions are unique due to no/less carrying over rules).
#   Incorrect outputs assigned to values after the loop (Final 3 instructions are unique due to less carrying over rules).
#   Likely awkward to adapt this to work when there are only 2 or 3 z values to output (not in the scope of the puzzle input).

data = [x.split('\n') for x in open('Input.txt', 'r').read().split('\n\n')]
unmodified_bits, start_instructions, x_bin, y_bin = {}, [v.split(' ') for v in data[1]], '', ''
for v in data[0]:
    unmodified_bits[v[0:3]] = int(v[5])
    if v[0] == 'x':
        x_bin = v[5] + x_bin
    else:
        y_bin = v[5] + y_bin
swapped_instructions = []

def get_arr_matches(elsewhere, arr):
    return [idx for idx, o in enumerate(arr) if o[0] in elsewhere and o[2] in elsewhere]
def get_swap_pair(elsewhere, arr):
    existing_value = [e for e in elsewhere if len([e for x in arr if e in [x[0], x[2]]]) > 0][0]
    other_key = [x[0] if existing_value == x[2] else x[2] for x in arr if existing_value in [x[0], x[2]]][0]
    return [[x for x in elsewhere if x != existing_value][0], other_key]

def search(unmodified_instructions):
    i_xor_xy, i_and_xy, i_and, i_or, i_xor = [], [], [], [], []
    for i in unmodified_instructions:
        if i[1] == 'XOR':
            if i[0][0] in ['x','y']: i_xor_xy.append(i)
            else: i_xor.append(i)
        elif i[1] == 'AND':
            if i[0][0] in ['x','y']: i_and_xy.append(i)
            else: i_and.append(i)
        else: i_or.append(i)
    
    i_xor_xy.sort(key=lambda x: x[0][1:])
    i_and_xy.sort(key=lambda x: x[0][1:])
    i_xor.sort(key=lambda x: x[4][1:])
    
    new_ord_i = [i_xor_xy[0], i_xor_xy[1], i_and_xy[0], i_xor.pop(0)]
    for i in range(len(i_xor_xy) - 2):
        new_ord_i += [i_xor_xy[i+2], i_and_xy[i+1]]
        
        and_elsewhere = [i_xor_xy[i+1][4], i_and_xy[i][4]] if i == 0 else [new_ord_i[-4][4], new_ord_i[-7][4]]
        and_matches = get_arr_matches(and_elsewhere, i_and)
        new_ord_i.append(i_and.pop(and_matches[0]))
        
        or_elsewhere = [new_ord_i[-1][4], new_ord_i[-2][4]]
        or_matches = get_arr_matches(or_elsewhere, i_or)
        if len(or_matches) == 0:
            return get_swap_pair(or_elsewhere, i_or)
        new_ord_i.append(i_or.pop(or_matches[0]))
        
        xor_elsewhere = [new_ord_i[-1][4], new_ord_i[-4][4]]
        xor_matches = get_arr_matches(xor_elsewhere, i_xor)
        if len(xor_matches) == 0:
            return get_swap_pair(xor_elsewhere, i_xor)
        
        new_ord_i.append(i_xor.pop(xor_matches[0]))
    new_ord_i += [i_and_xy[-1], i_and.pop(0), i_or.pop(0)]
    
    return None

while True:
    instructions = [x.copy() for x in start_instructions]
    for swap in swapped_instructions:
        for idx, x in enumerate(instructions):
            if x[4] == swap[0]:
                instructions[idx][4] = swap[1]
            elif x[4] == swap[1]:
                instructions[idx][4] = swap[0]
    
    swapped_instructions.append(search(instructions))
    if swapped_instructions[-1] == None:
        break
print(sorted([x for y in swapped_instructions[:-1] for x in y]))

bits, x_bin, y_bin = {}, '', ''
for x in data[0]:
    split = x.split(': ')
    bits[split[0]] = int(split[1])
    if split[0][0] == 'x':
        x_bin += str(bits[split[0]])
    else:
        y_bin += str(bits[split[0]])

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
expected_answer = int(x_bin[::-1], 2) + int(y_bin[::-1], 2)
program_answer = int(''.join([str(bits[x]) for x in sorted_keys[::-1]]), 2)
print(expected_answer)
print(program_answer)
print('Numbers are equal: ' + str(expected_answer == program_answer).upper())
