password = open('Input.txt', 'r').read()

min = 97
max = 122
numeric_password = [ord(x) for x in password]
invalid_chars = [105, 108, 111]

def password_is_valid(password):
    increasing_straight = False
    valid_chars = len([x for x in password if x in invalid_chars]) == 0
    pair_count = 0
    last_pair_index = 0
    
    for x in range(len(password) - 1):
        if x < len(password) - 2 and password[x] == password[x+1]-1 and password[x+1] == password[x+2]-1:
            increasing_straight = True
        
        if x > last_pair_index and password[x] == password[x+1]:
            pair_count += 1
            last_pair_index = x+1
    
    return increasing_straight and valid_chars and pair_count > 1

def add_to_password():
    for i in range(len(numeric_password))[::-1]:
        numeric_password[i] = min if numeric_password[i] == max else numeric_password[i] + 1 if numeric_password[i] + 1 not in invalid_chars else numeric_password[i] + 2
        
        if numeric_password[i] != min:
            break

def find_next_password():
    add_to_password()
    while not password_is_valid(numeric_password):
        add_to_password()
    print(''.join([chr(x) for x in numeric_password]))

find_next_password()
find_next_password()