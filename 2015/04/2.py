import hashlib

data = open('Input.txt', 'r').read()
tracker = 0

while True:
    if hashlib.md5((data + str(tracker)).encode()).hexdigest()[0:6:1].count('0') == 6:
        print(tracker)
        break
        
    tracker += 1