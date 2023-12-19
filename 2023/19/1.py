data = open('Input.txt', 'r').read().split('\n')
blank_line_reached = False

workflows = []
parts = []
for line in data:
    if line == '':
        blank_line_reached = True
    elif blank_line_reached:
        parts.append(line)
    else:
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

processed_parts = []
for part in parts:
    processed_part = {}
    for part_value in part[1:-1].split(','):
        key, value = part_value.split('=')
        processed_part[key] = int(value)
    processed_parts.append(processed_part)

ans = 0
for processed_part in processed_parts:
    current_key = 'in'
    while True:
        workflow = processed_workflows[current_key]
        
        for condition in workflow:
            if len(condition) == 4:
                part_value, operator, comparison_value, res = condition
                v = processed_part[part_value]
                if (v > comparison_value if operator == '>' else v < comparison_value):
                    next_key = res
                    break
            else:
                next_key = condition
                break
        
        if next_key == 'R':
            break
        elif next_key == 'A':
            ans += processed_part['x'] + processed_part['m'] + processed_part['a'] + processed_part['s']
            break
        else:
            current_key = next_key

print(ans)