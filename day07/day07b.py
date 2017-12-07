def tower(base):
    if base not in b.keys():
        return p[base]
    sum = 0
    temp = []
    for x in b[base]:
        if x not in t.keys():
            s = tower(x)
        else:
            s += t[x]
        temp.append(s)
        sum += s
    sum += p[base]
    if min(temp) != max(temp):
        print(temp, b[base],[p[x] for x in b[base]])
    return sum

with open('input.txt') as f:
    content = f.readlines()
p = {}
s = []
b = {}
t = {}
for line in content:
    parts = [x.replace(',','') for x in line.split()]
    p[parts[0]] = int(parts[1][1:-1])
    if len(parts) > 3:
        b[parts[0]] = []
        for x in parts[3:]:
            s.append(x)
            b[parts[0]].append(x)

bottom = set(p.keys()) - set(s)
bottom = bottom.pop()
print(bottom)
print(b)
print(tower(bottom))

