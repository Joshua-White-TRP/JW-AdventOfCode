data = open('Input.txt', 'r').read().split('\n')
char_to_points = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
}

splits = [[char_to_points[x[0]], char_to_points[x[2]]] for x in data]
ans = 0

for x in splits:
    ans += x[1]
    if x[0] == x[1]:
        ans += 3
    elif x[1] - 1 == x[0] or (x[1] == 1 and x[0] == 3):
        ans += 6
    
print(ans)