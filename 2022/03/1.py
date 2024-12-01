data = open('Input.txt', 'r').read().split('\n')
splits = [[x[0:int(len(x)/2)], x[int(len(x)/2):]] for x in data]
ans = 0

matched_piece = None
for split in splits:
    for x in split[0]:
        if x in split[1]:
            ans += ord(x) - (38 if x == x.upper() else 96)
            break

print(ans)