strings = open('Input.txt', 'r').read().split('\n')

nice_strings = 0

for s in strings:
    duplicate_pair = False
    gap_letter = False
    
    for idx, char in enumerate(s):
        if idx != len(s) - 1:
            pair = char + s[idx + 1]
            if pair in s.replace(pair, '  ', 1):
                duplicate_pair = True
            
        if idx < len(s) - 2 and char == s[idx + 2]:
            gap_letter = True
    
    if duplicate_pair and gap_letter:
        nice_strings += 1
        
print(nice_strings)