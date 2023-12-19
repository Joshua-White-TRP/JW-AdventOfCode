from math import prod
data = open('Input.txt', 'r').read().split('\n')
blank_line_reached = False

workflows = []
for line in data:
    if line == '':
        break
    workflows.append(line)

processed_workflows = {}
for workflow in workflows:
    key = workflow[:workflow.index('{')]
    split_rules = workflow[workflow.index('{')+1:-1].split(',')
    rules = []
    for r in split_rules:
        if ':' not in r:
            rules.append(r)
        else:
            cond, res = r.split(':')
            operator = '>' if '>' in cond else '<'
            part_value, comparison_value = cond.split(operator)
            
            rules.append([part_value, operator, int(comparison_value), res])
    
    processed_workflows[key] = rules

def diff_product(ranges):
    return prod([ranges[k][1] - ranges[k][0] + 1 for k in ranges])
def valid_range(range):
    return range[0] <= range[1]

def evaluate_workflow(ranges, key):
    if key == 'R':
        return 0
    elif key == 'A':
        return diff_product(ranges)
    
    fn_ans = 0
    fn_copy = ranges.copy()
    for condition in processed_workflows[key]:
        iter_copy = fn_copy.copy()
        if len(condition) == 4:
            part_value, operator, comparison_value, res = condition
            if operator == '>':
                iter_copy[part_value] = [comparison_value + 1, iter_copy[part_value][1]]
                fn_copy[part_value] = [fn_copy[part_value][0], comparison_value]
            else:
                iter_copy[part_value] = [iter_copy[part_value][0], comparison_value - 1]
                fn_copy[part_value] = [comparison_value, fn_copy[part_value][1]]
            
            if valid_range(iter_copy[part_value]):
                fn_ans += evaluate_workflow(iter_copy.copy(), res)
        else:
            fn_ans += evaluate_workflow(iter_copy, condition)
    
    return fn_ans

print(evaluate_workflow({ 'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000] }, 'in'))