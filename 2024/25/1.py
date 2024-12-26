data = [x.split('\n') for x in open('Input.txt', 'r').read().split('\n\n')]

num_locks, num_keys = [], []
for d in data:
    arr = [0,0,0,0,0]
    for row in d:
        for idx, i in enumerate(row):
            arr[idx] += int(i == '#')
    (num_locks if d[0][0] == '#' else num_keys).append(arr)

print(sum([sum([not any([l[i] + k[i] > 7 for i in range(0, 5)]) for k in num_keys]) for l in num_locks]))