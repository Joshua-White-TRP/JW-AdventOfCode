data = open('Input.txt', 'r').read().split('\n')

answer = 0
for line in data:
    numbers = sorted([int(x) for x in line.split('x')])
    
    l = numbers[0]
    w = numbers[1]
    h = numbers[2]
    
    shortest_side = l * w
    answer += shortest_side + 2 * shortest_side + 2 * w * h + 2 * h * l

print(answer)
    