from datetime import datetime

print(datetime.now())
data = open('Input.txt', 'r').read().split('\n')
time = int(''.join([x for x in data[0][data[0].find(':')+1::1].split(' ') if x != '']))
distance = int(''.join([x for x in data[1][data[1].find(':')+1::1].split(' ') if x != '']))

firstIndex = -1
secondIndex = -1
tracker = 0

while tracker < time:
    if tracker * (time - tracker) > distance:
        firstIndex = tracker
        break
    tracker += 1
    
tracker = time

while tracker > 0:
    if tracker * (time - tracker) > distance:
        secondIndex = tracker
        break
    tracker -= 1

print(datetime.now())
print(secondIndex - firstIndex + 1)