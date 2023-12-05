data = open('Input.txt', 'r').read().split('\n')
line_length = len(data[0])
joined_data = ''.join(data)
joined_data_length = len(joined_data)

answer = 0
tracked_number_text = ''
start_index = -1

for idx, x in enumerate(joined_data):
    if not x.isnumeric() and tracked_number_text == '':
        continue
    elif not x.isnumeric():
        index_adjustment = len(tracked_number_text)
        indexes_to_check = []
        while index_adjustment >= -1:
            index_value = start_index + index_adjustment
            indexes_to_check.append(index_value - line_length)
            indexes_to_check.append(index_value)
            indexes_to_check.append(index_value + line_length)
            index_adjustment -= 1
        
        for index_to_check in [a for a in indexes_to_check if a >= 0 and a < joined_data_length]:
            value_to_check = joined_data[index_to_check]
            if(not value_to_check.isnumeric() and not value_to_check == '.'):
                answer += int(tracked_number_text)
                break
        
        tracked_number_text = ''
        start_index = -1
    else:
        tracked_number_text += x
        if start_index == -1:
            start_index = idx

print(answer)