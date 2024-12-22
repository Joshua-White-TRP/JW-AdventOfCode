import functools
data = open('Input.txt', 'r').read().split('\n')
towels = data[0].split(', ')

@functools.cache
def search(p, text):
    results = 0
    for t in towels:
        new_text = text + t
        if new_text == p[:len(text) + len(t)]:
            results += 1 if new_text == p else search(p, new_text)
    return results

print(sum([search(p, '') for p in data[2:]]))