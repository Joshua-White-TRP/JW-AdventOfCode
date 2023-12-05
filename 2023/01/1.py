data = open('Input.txt', 'r').read().split('\n')
answers = []

for x in data:
    stripped_x = [y for y in x if y.isnumeric()]
    first_number = stripped_x[0]
    last_number = stripped_x[len(stripped_x)-1]
    answers.append(first_number + last_number)
    
answer = 0
for x in answers:
    answer += int(x)

print(answer)