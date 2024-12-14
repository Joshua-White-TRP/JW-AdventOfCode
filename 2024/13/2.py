data = open('Input.txt', 'r').read().split('\n')

puzzles = []
new_puzzle = []
coord_added_value = 10000000000000
for x in data:
    if "A:" in x or "B:" in x:
        new_puzzle.append([int(v.split('+')[1]) for v in x.split(', ')])
    elif "e:" in x:
        new_puzzle.append([int(v.split('=')[1]) + coord_added_value for v in x.split(', ')])
        puzzles.append(new_puzzle)
        new_puzzle = []

def search(coords_a, coords_b, destination):
    a_pressed, b_pressed, a, b = 0, 0, 0, 0
    press_count = coord_added_value
    
    while a < destination[0] and b < destination[1]:
        x_division, y_division = (destination[0] - a) / coords_a[0], (destination[1] - b) / coords_a[1]
        
        if x_division == y_division and x_division % 1 == 0:
            a, b, a_pressed = a + coords_a[0] * x_division, b + coords_a[1] * x_division, x_division
        else:
            new_a, new_b = a + coords_b[0] * press_count, b + coords_b[1] * press_count
            new_x_division, new_y_division = (destination[0] - new_a) / coords_a[0], (destination[1] - new_b) / coords_a[1]
            division_order_changed = (x_division > y_division) != (new_x_division > new_y_division)
            
            if press_count != 1 and division_order_changed:
                press_count /= 10
            elif division_order_changed:
                return None
            else:
                a, b, b_pressed = new_a, new_b, b_pressed + press_count
    
    return None if a != destination[0] or b != destination[1] else [a_pressed, b_pressed]
    
tickets_spent = 0
for puzzle in puzzles:
    priority_a = search(puzzle[0], puzzle[1], puzzle[2])
    priority_b = search(puzzle[1], puzzle[0], puzzle[2])
    
    priority_a_ans = None if priority_a == None else priority_a[0] * 3 + priority_a[1]
    priority_b_ans = None if priority_b == None else priority_b[1] * 3 + priority_b[0]
    
    if priority_a_ans != None and priority_b_ans == None:
        tickets_spent += priority_a_ans
    elif priority_a_ans == None and priority_b_ans != None:
        tickets_spent += priority_b_ans
    elif priority_a_ans != None and priority_b != None:
        tickets_spent += priority_a_ans if priority_a_ans < priority_b_ans else priority_b_ans

print(tickets_spent)