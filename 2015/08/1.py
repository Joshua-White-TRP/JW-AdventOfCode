data = open('Input.txt', 'r').read().split('\n')
escape_sequences = ['\\', '\"']

answer = 0
for line in data:
    index_tracker = 0
    answer += len(line) + 2
    
    while index_tracker < len(line):
        if line[index_tracker] == '\\':
            if line[index_tracker + 1] == 'x':
                index_tracker += 4
            else:
                index_tracker += 2
        else:
            index_tracker += 1
                
        answer -= 1


print(answer)