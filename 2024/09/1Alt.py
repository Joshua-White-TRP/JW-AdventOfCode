data = [int(x) for x in open('Input.txt', 'r').read().split('\n')[0]]

map = []
for i, x in enumerate(data):
    if i % 2 == 0:
        file_id = int(i / 2)
        for v in range(x):
            map.append(file_id)
    else:
        for v in range(x):
            map.append(None)

ans = 0
start_checker = 0
end_checker = len(map) - 1
while start_checker < end_checker:
    if map[start_checker] != None:
        ans += start_checker * map[start_checker]
    else:
        while map[end_checker] == None:
            end_checker -= 1
        ans += start_checker * map[end_checker]
        end_checker -= 1
    start_checker += 1

print(ans)