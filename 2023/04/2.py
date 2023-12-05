cards = open('Input.txt', 'r').read().split('\n')
card_count = len(cards)
card_matches = []
answer = 0

for card in cards:
    pipe_index = card.index('|')
    winning_numbers = [int(x) for x in card[card.index(':')+2:pipe_index - 1:1].split(' ') if x.isnumeric()]
    comparison_numbers = [int(x) for x in card[pipe_index+2::1].split(' ') if x.isnumeric()]
    
    matches = 0
    for winning_number in winning_numbers:
        if winning_number in comparison_numbers:
            matches += 1
    
    card_matches.append(matches)

def counut_cards(card_index):
    answer = 1
    matches = card_matches[card_index]
    
    while matches > 0:
        if card_index + matches < card_count:
            answer += counut_cards(card_index + matches)
        matches -= 1
        
    return answer

for idx, card in enumerate(card_matches):
    answer += counut_cards(idx)
    
print(answer)