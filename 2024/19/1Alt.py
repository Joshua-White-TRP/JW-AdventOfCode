import functools
data = open('Input.txt', 'r').read().split('\n')
towels = data[0].split(', ')

@functools.cache
def search(p, text):
    for t in towels:
        new_text = text + t
        if new_text == p[:len(text) + len(t)] and (new_text == p or search(p, new_text) == 1):
            return 1
    return 0

print(sum([search(p, '') for p in data[2:]]))