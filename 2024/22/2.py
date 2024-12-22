data = open('Input.txt', 'r').read().split('\n')

prune = 16777216
dic = {}
for d in data:
    num = int(d)
    s = [int(str(num)[-1])]
    for i in range(2000):
        num = (num ^ (num * 64)) % prune
        num = (num ^ int(num / 32)) % prune
        num = (num ^ (num * 2048)) % prune
        s.append(int(str(num)[-1]))
    
    unique_chains = set()
    for i in range(1, len(s) - 3):
        chain = tuple([s[j] - s[j-1] for j in range(i, i+4)])
        if chain not in unique_chains:
            unique_chains.add(chain)
            if chain not in dic:
                dic[chain] = 0
            dic[chain] += s[i+3]

print(max([dic[key] for key in dic]))