import functools
data = [int(x) for x in open('Input.txt', 'r').read().split('\n')[0].split(' ')]
ans = 0

@functools.cache
def search(num, depth):
    if depth == 75:
        return 1
    
    s = str(num)
    if num == 0:
        return search(1, depth + 1)
    elif len(s) % 2 == 0:
        halfway = int(len(s)/2)
        return search(int(s[:halfway]), depth + 1) + search(int(s[halfway:]), depth + 1)
    else:
        return search(num * 2024, depth + 1)
    
for x in data:
    ans += search(x, 0)
print(ans)