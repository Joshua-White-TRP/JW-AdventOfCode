data = open('Input.txt', 'r').read().split('\n')
total = 0
max = 0

for x in data:
    if x.isnumeric():
        total += int(x)
    else:
        if total > max:
            max = total
        total = 0

print(max)