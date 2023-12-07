from datetime import datetime

print(datetime.now())
data = open('Input.txt', 'r').read().split('\n')
time = int(''.join([x for x in data[0][data[0].find(':')+1::1].split(' ') if x != '']))
distance = int(''.join([x for x in data[1][data[1].find(':')+1::1].split(' ') if x != '']))

victory_total = 0
tracker = 0
while tracker < time:
    if tracker * (time - tracker) > distance:
        victory_total += 1
        
    tracker += 1

print(datetime.now())
print(victory_total)