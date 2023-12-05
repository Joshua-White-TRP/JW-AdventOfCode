data = open('Input.txt', 'r').read().split('\n')
number_strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
answers = []

for x in data:
    x_numbers = []
    letters = ''
    
    for y in x:
        letters += y
        
        if y.isnumeric():
            letters = ''
            x_numbers.append(y)
        elif len(letters) > 2:
            iterations = len(letters) - 3
            
            while (iterations >= 0):
                substring = letters[iterations::1]
                
                if substring in number_strings:
                    letters = letters[iterations+1::1]
                    x_numbers.append(str(number_strings.index(substring) + 1))
                    break
                    
                iterations -= 1
    
    first_number = x_numbers[0]
    last_number = x_numbers[len(x_numbers)-1]
    answers.append(first_number + last_number)
    
answer = 0
for x in answers:
    answer += int(x)

print(answer)