import math

codes = open('Input.txt', 'r').read().split('\n')
ds = [[-1,0],[1,0],[0,-1],[0,1]] # U D L R
ds_keypad_pos = [[0,1],[1,1],[1,0],[1,2]]

def sum_arr(a1, a2):
    return [a1[i] + a2[i] for i, v in enumerate(a1)]

def input_code(path, r_pos, is_numeric):
    instructions = []
    t = [x for x in r_pos]
    for ins in path:
        d_pos = ([3 - math.ceil(int(ins) / 3), 1 if ins == '0' else (int(ins) - 1) % 3] if ins != 'A' else [3,2]) if is_numeric else (ds_keypad_pos[ds.index(ins)] if ins != 'A' else [0,2])
        temp_instructions = [[],[]]
        validity_array = [True, True]
        
        for idx, i in enumerate([[0,1],[1,0]]):
            t2 = [x for x in t]
            for j in i:
                while t2[j] != d_pos[j]:
                    temp_instructions[idx].append(ds[j*2+1] if t2[j] < d_pos[j] else ds[j*2])
                    t2 = sum_arr(t2, temp_instructions[idx][-1])
                    if (is_numeric and t2 == [3,0]) or (not is_numeric and t2 == [0,0]):
                        validity_array[idx] = False
        
        t = [x for x in d_pos]
        if temp_instructions[0] == temp_instructions[1]:
            validity_array[1] = False
        instructions.append([x for idx, x in enumerate(temp_instructions) if validity_array[idx]])
        instructions.append('A')
    return instructions

ans = 0
for code in codes:
    instructions_to_try = [[input_code(code, [3,2], True),], [], []]
    final_paths = []
    
    for n in range(1,4):
        for instructions in instructions_to_try[n-1]:
            perms = [[]]
            for instruction in instructions:
                if instruction == 'A':
                    [p.append(instruction) for p in perms]
                    continue
                
                temp = [[z for z in y] if y != 'A' else 'A' for y in perms]
                split_length = len(temp)
                for i in range(len(instruction) - 1):
                    perms.extend([[z for z in y] if y != 'A' else 'A' for y in temp])
                
                for idx, permutation in enumerate(instruction):
                    for move in permutation:
                        [p.append(move) for p in perms[idx*split_length:(idx+1)*split_length]]
            
            if n < 3:                
                new_instructions = [input_code(p, [0,2], False) for p in perms]
                instructions_to_try[n].extend(new_instructions)
            else:
                final_paths.extend(perms)
    
    ans += min([len(f) for f in final_paths]) * int(code[:-1])
print(ans)