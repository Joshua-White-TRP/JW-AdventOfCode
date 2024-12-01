data = open('Input.txt', 'r').read().split('\n')
splits = [x.split('   ') for x in data]

left_list = [int(x[0]) for x in splits]
right_list = [int(x[1]) for x in splits]

index = 0
ans = 0

for x in left_list:
    for y in right_list:
        if x == y:
            ans += x
    
print(ans)