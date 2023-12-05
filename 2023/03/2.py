data = open('Input.txt', 'r').read().split('\n')
line_length = len(data[0])
joined_data = ''.join(data)
joined_data_length = len(joined_data)

answer = 0
tracked_number_text = ''

for idx, x in enumerate(joined_data):
    if x == '*':
        index_adjustment = 1
        indexes_to_check = []
        
        while index_adjustment >= -1:
            index_value = idx + index_adjustment
            indexes_to_check.append(index_value - line_length)
            indexes_to_check.append(index_value)
            indexes_to_check.append(index_value + line_length)
            index_adjustment -= 1
            
        indexes_to_check = [a for a in indexes_to_check if a >= 0 and a < joined_data_length]
        indexes_to_check.sort()
        
        numbers_detected = []
        latest_checked_index = 0
        for index_to_check in indexes_to_check:
            if index_to_check <= latest_checked_index:
                continue
            
            if joined_data[index_to_check].isnumeric():
                new_index = index_to_check - 1
                new_number = ''
                
                while(joined_data[new_index].isnumeric()):
                    new_index -= 1
                    
                while(joined_data[new_index+1].isnumeric()):
                    new_number += joined_data[new_index+1]
                    new_index += 1
                latest_checked_index = new_index + 1
                
                numbers_detected.append(new_number)
            
        
        if len(numbers_detected) == 2:
            answer += int(numbers_detected[0]) * int(numbers_detected[1])

print(answer)