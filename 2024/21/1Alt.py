import math

codes = open('Input.txt', 'r').read().split('\n')
ds = [[-1,0],[1,0],[0,-1],[0,1]] # U D L R
ds_keypad_pos = [[0,1],[1,1],[1,0],[1,2]]
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

def dirpad_map(c, d):
    if c == d:
        return 'A'
    elif (c == 'A' and d == '^') or (c == '>' and d == 'v') or (c == 'v' and d == '<'):
        return '<A'
    elif (c == '^' and d == 'v') or (c == 'A' and d == '>'):
        return 'vA'
    elif (c == '<' and d == 'v') or (c == 'v' and d == '>') or (c == '^' and d == 'A'):
        return '>A'
    elif (c == '>' and d == 'A') or (c == 'v' and d == '^'):
        return '^A'
    elif c == 'A':
        return '<vA' if d == 'v' else 'v<<A'
    elif c == '^':
        return 'v>A' if d == '>' else 'v<A'
    elif c == '>':
        return '<^A' if d == '^' else '<<A'
    elif c == 'v':
        return '^>A'
    elif c == '<':
        return '>^A' if d == '^' else ('>^A' if d == '>' else '>>^A')

ans = 0
for code in codes:
    moves = code
    for i in range(0, 3):
        new_moves, pos = '', 'A'
        for m in moves:
            new_moves += dirpad_map(pos, m) if i > 0 else numpad_map(pos, m)
            pos = m
        moves = new_moves
    ans += len(moves) * int(code[:-1])
    
print(ans)