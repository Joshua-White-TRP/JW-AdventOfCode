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

while '.' in map:
    last_value = map[-1]
    if last_value != '.':
        map[map.index('.')] = last_value
    map = map[:-1]

ans = 0
for idx, x in enumerate(map):
    ans += idx * int(x)
print(ans)