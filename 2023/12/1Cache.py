from functools import cache
data = open('Input.txt', 'r').read().split('\n')
answer = 0

@cache
def evaluate_spring(split_springs, broken_groups):
    if len(split_springs) == 0 and len(broken_groups) == 0:
        return 1
    elif all([True if x == '?' else False for x in ''.join(split_springs)]) and len(broken_groups) == 0:
        return 1
    elif len(split_springs) == 0 or len(broken_groups) == 0:
        return 0
    elif len(split_springs[0]) == broken_groups[0]:
        temp_ans = 0
        if all([True if x == '?' else False for x in split_springs[0]]):
            temp_ans += evaluate_spring(split_springs[1:], broken_groups)
        return temp_ans + evaluate_spring(split_springs[1:], broken_groups[1:])
    elif len(split_springs[0]) < broken_groups[0]:
        if not all([True if x == '?' else False for x in split_springs[0]]):
            return 0
        return evaluate_spring(split_springs[1:], broken_groups)
    else:
        s = split_springs[0]
        b = broken_groups[0]
        has_hashtag = not all([True if x == '?' else False for x in s])
        temp_ans = 0
        
        if not has_hashtag:
            temp_ans += evaluate_spring(split_springs[1:], broken_groups)
        
        for i in range(0, len(s) - b + 1):
            if i + b == len(s):
                if i-1 < 0 or s[i-1] != '#':
                    temp_ans += evaluate_spring(split_springs[1:], broken_groups[1:])
            elif (i-1 < 0 or s[i-1] != '#') and s[i+b] != '#':
                temp_ans += evaluate_spring(tuple([s[i+b+1:]] + list(split_springs[1:])) if i+b+1 < len(s) else split_springs[1:], broken_groups[1:])
                
            if s[i] == '#':
                break
        return temp_ans

for line in data:
    split_line = line.split(' ')
    springs = split_line[0]
    split_springs = tuple([x for x in split_line[0].split('.') if x.replace('.', '') != ''])
    broken_groups = tuple([int(x) for x in split_line[1].split(',')])
    
    answer += evaluate_spring(split_springs, broken_groups)

print(answer)