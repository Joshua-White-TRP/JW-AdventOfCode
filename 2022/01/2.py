data = open('Input.txt', 'r').read().split('\n')
total = 0
totals = []

for x in data:
    if x.isnumeric():
        total += int(x)
    else:
        totals.append(total)
        total = 0

totals.sort(reverse = True)
print(sum(totals[0:3]))