#This was my initial solution to d24p2. It gave me the info needed to manually locate the required swaps.
#The Input file was duplicated and the replacement was made inside this new file (e.g. Input2.txt).
#This process was repeated until all 4 errors were found and the program output all instructions in the correct order.
#
#TL:DR; this program can only help you manually spot the problem.
#Perform replacements manually in the Input and rerun until you find all 4.

data = open('Input.txt', 'r').read().split('\n')
unmodified_bits = {}
unmodified_instructions = []

after_blank = False
for x in data:
    if x == '':
        after_blank = True
        continue
    
    if after_blank:
        unmodified_instructions.append(x.split(' '))
    else:
        split = x.split(': ')
        unmodified_bits[split[0]] = int(split[1])

i_z, i_xor, i_and_xy, i_and, i_or, i_other = [], [], [], [], [], []
for i in unmodified_instructions:
    if i[4][0] == 'z':
        i_z.append(' '.join(i))
    elif i[1] == 'XOR' and i[0][0] in ['x','y']:
        i_xor.append(' '.join(i))
    elif i[1] == 'AND':
        if i[0][0] in ['x','y']:
            i_and_xy.append(' '.join(i))
        else:
            i_and.append(' '.join(i))
    elif i[1] == 'OR':
        i_or.append(' '.join(i))
    else:
        i_other.append(' '.join(i))

i_z.sort(key=lambda x: x.split(' ')[4][1:])
i_xor.sort(key=lambda x: x[1:])
i_and_xy.sort(key=lambda x: x[1:])
used_i_or = []
used_i_and = []

print()
for i in range(max([len(i_z), len(i_and_xy), len(i_xor)])):
    if i < len(i_z):
        print(i_z[i])
    print()
    
    if i < len(i_xor):
        print(i_xor[i])
    if i < len(i_and_xy):
        print(i_and_xy[i])
    
    if i <= len(i_and):
        z = i_z[i]
        z_split = z.split(' ')
        a, b = z_split[0], z_split[2]
        ins_and = [o for o in i_and if o.split(' ')[0] in [a, b] and o.split(' ')[2] in [a, b]]
        if len(ins_and) > 0:
            print(ins_and[0])
            used_i_and.append(ins_and[0])
    if i < len(i_xor):
        z = i_z[i+1]
        z_split = z.split(' ')
        a, b = z_split[0], z_split[2]
        key_to_check = a if a != i_xor[i][len(z)-3:] else b
        
        ins_or = [o for o in i_or if o.split(' ')[4] == key_to_check]
        if len(ins_or) > 0:
            print(ins_or[0])
            used_i_or.append(ins_or[0])

print('\nUnused AND')
[print(x) for x in i_and if x not in used_i_and]
print('\n\nUnused OR')
[print(x) for x in i_or if x not in used_i_or]
print('\n\nUNKNOWN')
[print(x) for x in i_other]