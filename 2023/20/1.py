data = open('Input.txt', 'r').read().split('\n')

module_states = {}
module_details = {}
for line in data:
    m, d = line.split(' -> ')
    destinations = d.split(', ')
    
    if m[0] == '%':
        module_name = m[1:]
        module_type = 0
    elif m[0] == '&':
        module_name = m[1:]
        module_type = 1
    else:
        module_name = m
        module_type = 2
    
    module_states[module_name] = False
    module_details[module_name] = [module_type, destinations, {}]

for key in module_details:
    for d in module_details[key][1]:
        if d in module_details:
            module_details[d][2][key] = False

low_count = 0
high_count = 0

def press_button():
    global low_count
    global high_count
    c_type, c_dest, _ = module_details['broadcaster']
    
    q = [['broadcaster', c_type, c_dest, False]]
    while q:
        sender, type, dests, signal = q.pop(0)

        for d in dests:
            if not signal:
                low_count += 1
            else:
                high_count +=1
            
            if d not in module_states:
                continue
            
            n_state = module_states[d]
            n_type, n_dest, n_arr = module_details[d]
            
            if n_type == 0:
                if not signal:
                    module_states[d] = not n_state
                    q.append([d, n_type, n_dest, module_states[d]])
            elif n_type == 1:
                module_details[d][2][sender] = signal
                if all([module_details[d][2][key] for key in module_details[d][2]]):
                    q.append([d, n_type, n_dest, False])
                else:
                    q.append([d, n_type, n_dest, True])

for i in range(1000):
    low_count += 1
    press_button()

print(low_count * high_count)