from collections import Counter

data = open('Input.txt', 'r').read().split('\n')
pairs = [x.split(' ') for x in data]
card_priorities = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

type_arrays = [[],[],[],[],[]] #worst to best hand 1-5 of a kind
full_houses = []
two_pairs = []

for pair in pairs:
    card_dict = Counter(pair[0])
    card_values = list(card_dict.values())
    card_values.sort(reverse=True)
    
    j_count = card_dict['J'] if 'J' in card_dict else 0
    if j_count > 0:
        card_values.remove(j_count)
    
    if len(card_values) <= 1:
        type_arrays[4].append(pair)
    elif card_values[1] == 2 and card_values[0] == 3 - j_count:
        full_houses.append(pair)
    elif card_values[0] == 2 and card_values[1] == 2:
        two_pairs.append(pair)
    else:
        type_arrays[card_values[0] + j_count - 1].append(pair)

type_arrays.insert(2, two_pairs)
type_arrays.insert(4, full_houses)
    
sorted_pairs = []
for type_array in type_arrays:
    sorted_pairs += sorted(type_array, key=lambda x: [card_priorities.index(y) for y in x[0]], reverse=True)

answer = 0
for idx, pair in enumerate(sorted_pairs):
    answer += (idx + 1) * int(pair[1])

print(answer)