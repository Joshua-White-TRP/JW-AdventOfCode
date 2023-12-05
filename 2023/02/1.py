games = open('Input.txt', 'r').read().split('\n')
cube_colours = ['red', 'green', 'blue']
cube_limits = [12, 13, 14]
answer = 0

for game in games:
    colon_index = game.find(':')
    space_index = game.find(' ')
    id_stripped_game = game[colon_index+2::1]
    game_id = game[space_index+1:colon_index:1]
    
    rounds = id_stripped_game.replace(' ', '').split(';')
    valid_game = True
    
    for round in rounds:
        cube_counts = [0, 0, 0]
        draws = round.split(',')
        for draw in draws:
            number = ''.join([x for x in draw if x.isnumeric()])
            colour = draw[len(number)::1]
            
            colour_index = cube_colours.index(colour)
            if cube_limits[colour_index] < int(number):
                valid_game = False
                break
        
        if not valid_game:
            break
    
    if valid_game:
        answer += int(game_id)

print(answer)