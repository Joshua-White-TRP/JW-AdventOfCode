data = open('Input.txt', 'r').read()

openCount = 0
closedCount = 0

for idx, x in enumerate(data):
    if x == '(':
        openCount += 1
    elif x == ')':
        closedCount += 1
        
    if openCount - closedCount == -1:
        print(idx + 1)
        break