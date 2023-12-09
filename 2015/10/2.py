current_value = open('Input.txt', 'r').read()

for i in range(50):
    new_value = ''
    track = ''
    
    for x in current_value:
        if not (track == '' or x == track[0]):
            new_value += str(len(track)) + track[0]
            track = ''
        track += x
    
    current_value = new_value + str(len(track)) + track[0]

print(len(current_value))