data = open('Input.txt', 'r').read().split('\n')
splits = [x.split('   ') for x in data]

left_list = [int(x[0]) for x in splits]
right_list = [int(x[1]) for x in splits]

print(sum([left_list.count(x) * x for x in right_list]))