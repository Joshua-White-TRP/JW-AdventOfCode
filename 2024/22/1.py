data = open('Input.txt', 'r').read().split('\n')

ans = 0
prune = 16777216
for d in data:
    num = int(d)
    for i in range(2000):
        num = (num ^ (num * 64)) % prune
        num = (num ^ int(num / 32)) % prune
        num = (num ^ (num * 2048)) % prune
    ans += num
print(ans)