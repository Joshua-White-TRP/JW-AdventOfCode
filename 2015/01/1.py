data = open('Input.txt', 'r').read()

openCount = 0
closedCount = 0

for x in data:
    if x == '(':
        openCount += 1
    elif x == ')':
        closedCount += 1
        
print(openCount - closedCount)