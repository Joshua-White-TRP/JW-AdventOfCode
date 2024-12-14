data = open('Input.txt', 'r').read().split('\n')

puzzles = []
new_puzzle = []
for x in data:
    if "A:" in x or "B:" in x:
        new_puzzle.append([int(v.split('+')[1]) for v in x.split(', ')])
    elif "e:" in x:
        new_puzzle.append([int(v.split('=')[1]) + coord_added_value for v in x.split(', ')])
        puzzles.append(new_puzzle)
        new_puzzle = []

def cramers_calc(coords_a, coords_b, destination):
    divisor = coords_a[0] * coords_b[1] - coords_a[1] * coords_b[0]
    return [
        (destination[0] * coords_b[1] - destination[1] * coords_b[0]) / divisor,
        (coords_a[0] * destination[1] - coords_a[1] * destination[0]) / divisor
    ]

ans = 0
for puzzle in puzzles:
    a, b = cramers_calc(puzzle[0], puzzle[1], puzzle[2])
    if a % 1 == 0 and b % 1 == 0:
        ans += a*3 + b

print(ans)