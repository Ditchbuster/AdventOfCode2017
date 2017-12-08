with open('input.txt') as f:
    content = f.readlines()
reg = {}

for line in content:
    parts = [x for x in line.split()]
    if parts[0] not in reg.keys():
        reg[parts[0]] = 0
    if parts[4] not in reg.keys():
        reg[parts[4]] = 0
    c = parts[5]
    vaild = False
    if c == '>':
        if reg[parts[4]] > int(parts[6]):
            vaild = True
    elif c == '<':
        if reg[parts[4]] < int(parts[6]):
            vaild = True
    elif c == '>=':
        if reg[parts[4]] >= int(parts[6]):
            vaild = True
    elif c == '<=':
        if reg[parts[4]] <= int(parts[6]):
            vaild = True
    elif c == '==':
        if reg[parts[4]] == int(parts[6]):
            vaild = True
    elif c == '!=':
        if reg[parts[4]] != int(parts[6]):
            vaild = True

    if vaild:
        if parts[1] == 'inc':
            reg[parts[0]] += int(parts[2])
        else:
            reg[parts[0]] -= int(parts[2])

print(max(reg.values()))