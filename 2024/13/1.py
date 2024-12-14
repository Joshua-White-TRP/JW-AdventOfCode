data = open('Input.txt', 'r').read().split('\n')

puzzles = []
new_puzzle = []
for x in data:
    if "A:" in x or "B:" in x:
        new_puzzle.append([int(v.split('+')[1]) for v in x.split(', ')])
    elif "e:" in x:
        new_puzzle.append([int(v.split('=')[1]) for v in x.split(', ')])
        puzzles.append(new_puzzle)
        new_puzzle = []

def search(coords_a, coords_b, destination):
    a_pressed, b_pressed = 0, 0
    a, b = 0, 0
    
    while a < destination[0] and b < destination[1]:
        x_division = (destination[0] - a) / coords_a[0]
        y_division = (destination[1] - b) / coords_a[1]
        if coords_a in [puzzles[0][0], puzzles[0][1]]:
            print('------')
            print(str(a) + ', ' + str(b) + ' ----- ' + str(destination[0]) + ', ' + str(destination[1]))
            print(str(x_division) + ' and ' + str(y_division))
            #print(str(a_pressed) + ' vs ' + str(b_pressed))
            print(b_pressed)
        
        if x_division == y_division and x_division % 1 == 0:
            a += coords_a[0] * x_division
            b += coords_a[1] * x_division
            a_pressed += x_division
        else:
            a += coords_b[0]
            b += coords_b[1]
            b_pressed += 1
    
    if a != destination[0] or b != destination[1]:
        return None
    else:
        return [a_pressed, b_pressed]

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