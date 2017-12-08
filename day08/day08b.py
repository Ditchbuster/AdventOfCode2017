with open('input.txt') as f:
    content = f.readlines()
reg = {}
maxx = 0
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
        if reg[parts[0]] > maxx:
            maxx = reg[parts[0]]
print(max(reg.values()),maxx)