data = open('Input.txt', 'r').read().split('\n')

answer = 0
for line in data:
    numbers = sorted([int(x) for x in line.split('x')])
    
    l = numbers[0]
    w = numbers[1]
    h = numbers[2]
    
    answer += 2 * l + 2 * w + l * w * h

print(answer)
    