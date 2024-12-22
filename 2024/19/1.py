data = open('Input.txt', 'r').read().split('\n')
towels = data[0].split(', ')
patterns = data[2:]
unique_attempts = []

def search(p, texts):
    unique_attempts.extend(texts)
    attempts = []
    for text in texts:
        for t in towels:
            if text + t == p[:len(text) + len(t)]:
                attempts.append(text + t)
    
    if len(attempts) == 0:
        return False
    if any([x == p for x in attempts]):
        return True
    return search(p, [a for a in set(attempts) if a not in unique_attempts])

ans = 0
for p in patterns:
    unique_attempts = []
    ans += int(search(p, ['']))

print(ans)