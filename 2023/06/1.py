data = open('Input.txt', 'r').read().split('\n')
times = [int(x) for x in data[0][data[0].find(':')+1::1].split(' ') if x != '']
distances = [int(x) for x in data[1][data[1].find(':')+1::1].split(' ') if x != '']

victory_totals = []
for idx, time in enumerate(times):
    victory_totals.append(0)
    distance = distances[idx]
    tracker = 0
    
    while tracker < time:
        if tracker * (time - tracker) > distance:
            victory_totals[idx] += 1
            
        tracker += 1

answer = victory_totals[0]
for victory_total in victory_totals[1::1]:
    answer *= victory_total
    
print(answer)