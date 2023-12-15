data = [[y for y in x] for x in open('Input.txt', 'r').read().split('\n')]
row_count = len(data)
answer = 0

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] != 'O':
            continue
        
        i_track = i
        while i_track > 0 and data[i_track-1][j] == '.':
            data[i_track][j] = '.'
            i_track -= 1
            data[i_track][j] = 'O'
        answer += row_count - i_track

print(answer)