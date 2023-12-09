data = open('Input.txt', 'r').read().split('\n')
escape_sequences = ['\\', '\"']

answer = 0
for line in data:
    index_tracker = 0
    
    while index_tracker < len(line):
        if line[index_tracker] == '\"':
            answer += 2
        elif line[index_tracker] == '\\':
            if line[index_tracker + 1] in escape_sequences:
                answer += 2
                index_tracker += 1
            elif line[index_tracker + 1] == 'x':
                answer += 1

        index_tracker += 1

print(answer)