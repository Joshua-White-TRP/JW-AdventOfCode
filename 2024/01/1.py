data = open('Input.txt', 'r').read().split('\n')
splits = [x.split('   ') for x in data]

left_list = [int(x[0]) for x in splits]
right_list = [int(x[1]) for x in splits]
left_list.sort()
right_list.sort()

index = 0
ans = 0
while index < len(right_list):
    ans += abs(left_list[index] - right_list[index])
    index += 1
    
print(ans)