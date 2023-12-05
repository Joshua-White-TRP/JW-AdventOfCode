games = open('Input.txt', 'r').read().split('\n')
cube_colours = ['red', 'green', 'blue']
cube_limits = [12, 13, 14]
answer = 0

for game in games:
    minimums = [0, 0, 0]
    colon_index = game.find(':')
    space_index = game.find(' ')
    id_stripped_game = game[colon_index+2::1]
    game_id = game[space_index+1:colon_index:1]
    
    rounds = id_stripped_game.replace(' ', '').split(';')
    
    for round in rounds:
        cube_counts = [0, 0, 0]
        draws = round.split(',')
        for draw in draws:
            number_text = ''.join([x for x in draw if x.isnumeric()])
            number = int(number_text)
            colour = draw[len(number_text)::1]
            
            colourIndex = cube_colours.index(colour)
            if minimums[colourIndex] < number:
                minimums[colourIndex] = number
                
    answer += minimums[0] * minimums[1] * minimums[2]

print(answer)