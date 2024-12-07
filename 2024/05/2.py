data = open('Input.txt', 'r').read().split('\n')
ordering_rules = []
updates = []
ans = 0

for x in data:
    if '|' in x:
        ordering_rules.append(x.split('|'))
    elif ',' in x:
        updates.append(x.split(','))

for update in updates:
    is_valid = True
    x = 0
    
    while x < len(update) - 1:
        y = x + 1
        while y < len(update):
            if [update[y], update[x]] in ordering_rules:
                is_valid = False
                temp = update[x]
                update[x] = update[y]
                update[y] = temp
                x -= 1
                break
            y += 1
        x += 1
    
    if not is_valid:
        ans += int(update[int((len(update) - 1) / 2)])

print(ans)