import itertools

data = open('Input.txt', 'r').read().split('\n')
answer = 0
maximum = 0
hashmap = {}

def generate_hashmap_values(springs):
    global maximum
    spring_combinations = []
    question_indexes = [idx for idx, x in enumerate(springs) if x == '?']
    question_count = len(question_indexes)
    hash_count = len([idx for idx, x in enumerate(springs) if x == '#'])
    
    for i in range(1, (question_count if question_count < maximum - hash_count else maximum - hash_count) + 1):
        for comb in [x for x in itertools.combinations(question_indexes, i)]:
            spring_combinations.append(''.join(['#' if idx not in comb else '.' for idx, x in enumerate(springs)]))
    
    all_hashtag = ''.join(['#' for x in springs])
    if all_hashtag not in spring_combinations:
        spring_combinations.append(all_hashtag)

    for spring_comb in spring_combinations:
        hashmap_key_b = tuple([len(x) for x in spring_comb.split('.') if x.replace('.','') != ''])
        
        if springs not in hashmap:
            hashmap[springs] = {}
        
        if hashmap_key_b not in hashmap[springs]:
            hashmap[springs][hashmap_key_b] = 0
        
        hashmap[springs][hashmap_key_b] += 1

def evaluate_spring(split_springs, broken_groups, routes):
    global answer
    
    if (len(split_springs) == 0 and len(broken_groups) == 0) or (all([True if x == '?' else False for x in ''.join(split_springs)]) and len(broken_groups) == 0):
        answer += routes
        return
    elif len(split_springs) == 0 and len(broken_groups) > 0:
        return

    s = split_springs[0]
    if s not in hashmap:
        generate_hashmap_values(s)
    if all([True if x == '?' else False for x in s]):
        evaluate_spring(split_springs[1:], broken_groups[0:], routes)
        
    broken_groups_index = 0
    broken_groups_total = 0

    while broken_groups_index < len(broken_groups):
        broken_groups_total += broken_groups[broken_groups_index]
        if broken_groups_total + broken_groups_index > len(s):
            break
        
        spring_map = hashmap[s]
        broken_groups_tuple = tuple([x for x in broken_groups[:broken_groups_index+1]])
        
        if broken_groups_tuple in spring_map:
            evaluate_spring(split_springs[1:], broken_groups[broken_groups_index+1:], routes * spring_map[broken_groups_tuple])
        
        broken_groups_index += 1
    
for line in data:
    broken_groups_max = max([int(x) for x in line.split(' ')[1].split(',')])
    if broken_groups_max > maximum:
        maximum = broken_groups_max

for line in data:
    split_line = line.split(' ')
    split_springs = [x for x in split_line[0].split('.') if x.replace('.', '') != '']
    broken_groups = [int(x) for x in split_line[1].split(',')]
    
    evaluate_spring(split_springs, broken_groups, 1)

print(answer)