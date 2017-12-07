with open('input.txt') as f:
    content = f.readlines()
p = []
s = []
for line in content:
    parts = [x.replace(',','') for x in line.split()]
    p.append(parts[0])
    if len(parts) > 3:
        for x in parts[3:]:
            s.append(x)

print(set(p) - set(s))