data = open('Input.txt', 'r').read().split('\n')
ans = 0
index = 2

while index <= len(data):
    for x in data[index-2]:
        if x in data[index-1] and x in data[index]:
            ans += ord(x) - (38 if x == x.upper() else 96)
            index += 3
            break

print(ans)