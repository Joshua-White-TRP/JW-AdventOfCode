import sys
import math
import functools
sys.setrecursionlimit(10000000)

codes = open('Input.txt', 'r').read().split('\n')
numpad_positions = [[3,1],[2,0],[2,1],[2,2],[1,0],[1,1],[1,2],[0,0],[0,1],[0,2]]

def numpad_map(c, d):
    c_loc = [x for x in numpad_positions[int(c)]] if c != 'A' else [3,2]
    d_loc = [x for x in numpad_positions[int(d)]] if d != 'A' else [3,2]
    
    directions = ''
    if c in '147' and d in '0A':
        while c_loc[1] < d_loc[1]:
            c_loc[1] += 1
            directions += '>'
        while c_loc[0] < d_loc[0]:
            c_loc[0] += 1
            directions += 'v'
    elif c in '0A' and d in '147':
        while c_loc[0] > d_loc[0]:
            c_loc[0] -= 1
            directions += '^'
        while c_loc[1] > d_loc[1]:
            c_loc[1] -= 1
            directions += '<'
    else:
        while c_loc[1] > d_loc[1]:
            c_loc[1] -= 1
            directions += '<'
        while c_loc[0] < d_loc[0]:
            c_loc[0] += 1
            directions += 'v'
        while c_loc[0] > d_loc[0]:
            c_loc[0] -= 1
            directions += '^'
        while c_loc[1] < d_loc[1]:
            c_loc[1] += 1
            directions += '>'
    
    return directions + 'A'

#Apply instructions in order of LDUR (prioritise furthest from 'A' on directional keypad).
#The LDUR rule is only broken if it would cross the blank space as zig-zagging directions is less efficient.
dirpad_dict = { 
    ('A','A'): 'A',
    ('^','^'): 'A',
    ('>','>'): 'A',
    ('<','<'): 'A',
    ('v','v'): 'A',
    ('A','^'): '<A',
    ('>','v'): '<A',
    ('v','<'): '<A',
    ('^','v'): 'vA',
    ('A','>'): 'vA',
    ('^','A'): '>A',
    ('v','>'): '>A',
    ('<','v'): '>A',
    ('v','^'): '^A',
    ('>','A'): '^A',
    ('A','<'): 'v<<A',
    ('A','v'): '<vA',
    ('^','<'): 'v<A',
    ('^','>'): 'v>A',
    ('>','<'): '<<A',
    ('>','^'): '<^A',
    ('v','A'): '^>A',
    ('<','A'): '>>^A',
    ('<','>'): '>>A',
    ('<','^'): '>^A',
}

@functools.cache
def dirpad_map_sequence(seq, depth):
    if depth == 0:
        return len(seq)
    
    move_length, pos = 0, 'A'
    for m in seq:
        move_length += dirpad_map_sequence(dirpad_dict[(pos, m)], depth - 1)
        pos = m
        
    return move_length

ans = 0
for code in codes:
    moves, pos = '', 'A'
    for c in code:
        moves += numpad_map(pos, c)
        pos = c
    
    total = 0
    for m in moves.split('A')[:-1]:
        total += dirpad_map_sequence(m + 'A', 25)
    ans += total * int(code[:-1])
    
print(ans)
