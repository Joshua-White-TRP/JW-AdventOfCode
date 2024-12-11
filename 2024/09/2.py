data = [int(x) for x in open('Input.txt', 'r').read().split('\n')[0]]
print(data)

map = []
for i, x in enumerate(data):
    if i % 2 == 0:
        file_id = int(i / 2)
        for v in range(x):
            map.append(file_id)
    else:
        for v in range(x):
            map.append('.')

last_checked_value = max([x for x in map if x != '.']) + 1
print(map)
while last_checked_value > 0:
    print(last_checked_value)
    new_value = last_checked_value - 1
    first_index_of_value = map.index(new_value)
    arr = [idx for idx, x in enumerate(map) if x == new_value]
    
    for i in range(first_index_of_value - len(arr) + 1):
        if all([x == '.' for x in map[i:i+len(arr)]]):
            for j in range(i, i+len(arr)):
                map[j] = new_value
            
            for j in arr:
                map[j] = '.'
            break
    
    last_checked_value = new_value

print(map)

ans = 0
for idx, x in enumerate(map):
    if x != '.':
        ans += idx * int(x)
print(ans)
print(map)