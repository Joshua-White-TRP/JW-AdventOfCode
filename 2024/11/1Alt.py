data = [int(x) for x in open('Input.txt', 'r').read().split('\n')[0].split(' ')]
cache = {}
ans = 0

def search(num, depth):
    if depth == 25:
        return 1
    
    if (num, depth) not in cache:
        s = str(num)
        if num == 0:
            cache[(num, depth)] = search(1, depth + 1)
        elif len(s) % 2 == 0:
            halfway = int(len(s)/2)
            cache[(num, depth)] = search(int(s[:halfway]), depth + 1) + search(int(s[halfway:]), depth + 1)
        else:
            cache[(num, depth)] = search(num * 2024, depth + 1)
    
    return cache[(num, depth)]
    
for x in data:
    ans += search(x, 0)
print(ans)