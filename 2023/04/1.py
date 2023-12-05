cards = open('Input.txt', 'r').read().split('\n')
card_points = []
answer = 0

for card in cards:
    points = 0
    pipe_index = card.index('|')
    winning_numbers = [int(x) for x in card[card.index(':')+2:pipe_index - 1:1].split(' ') if x.isnumeric()]
    comparison_numbers = [int(x) for x in card[pipe_index+2::1].split(' ') if x.isnumeric()]
    
    for winning_number in winning_numbers:
        if winning_number in comparison_numbers:
            if points == 0:
                points = 1
            else:
                points *= 2
    
    if points > 0:
        answer += points

print(answer)