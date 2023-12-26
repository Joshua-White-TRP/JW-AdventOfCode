from json import loads

def evaluate_type_switch(n):
    t = type(n)
    if t is str and n.isnumeric():
        return int(n)
    elif t is int:
        return n
    elif t is list:
        return sum([evaluate_type_switch(i) for i in n])
    elif t is dict and all([n[k] != 'red' for k in n]):
        return sum([evaluate_type_switch(n[k]) for k in n])
    return 0

print(evaluate_type_switch(loads(open('Input.txt', 'r').read())))