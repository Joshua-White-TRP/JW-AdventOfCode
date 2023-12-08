strings = open('Input.txt', 'r').read().split('\n')

nice_strings = 0
bad_pairs = ['ab', 'cd', 'pq', 'xy']

for s in strings:
    vowel_count = 0
    double_letter = False
    pairs_rule = len([pair for pair in bad_pairs if pair in s]) == 0
    
    for idx, char in enumerate(s):
        if char in 'aeiou':
            vowel_count += 1
            
        if idx != len(s) - 1 and char == s[idx + 1]:
            double_letter = True
    
    if vowel_count >= 3 and double_letter and pairs_rule:
        nice_strings += 1
        
print(nice_strings)