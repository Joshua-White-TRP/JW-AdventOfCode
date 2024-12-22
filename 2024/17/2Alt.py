data = open('Input.txt', 'r').read().split('\n')
programs = [int(x) for x in data[4].split(': ')[1].split(',')]
programs.reverse()
vs = [1]
for x in programs:
    vs.append(vs[-1] * 8)

tracker = 0
ranges = [[1,8]]
while True:
    valid_nums = []
    for r in ranges:
        for a in range(r[0], r[1]):
            b = (a % 8) ^ 5
            c = int(a / (2**b))
            if ((b ^ 6) ^ c) % 8 == programs[tracker]:
                valid_nums.append(a)
    ranges = [[v * 8, (v+1)*8] for v in valid_nums]
    tracker += 1
    
    if tracker == 16:
        print(min(valid_nums))
        break