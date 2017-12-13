with open('input.txt') as f:
    content = f.readlines()
wall = {}
scanner = {}
for line in content:
    parts = [int(x) for x in line.replace(':','').split()]
    wall[parts[0]] = parts[1]
    scanner[parts[0]] = [1,1] # pos, dir


max = max(wall.keys())
caught = []
pos = -1
cat = False
while pos <= max:
    pos += 1
    if pos in scanner.keys():
        if scanner[pos][0] == 1: #caught
            caught.append(pos)
            cat = True
    for s,val in scanner.items():
        val[0] += val[1]
        if 1 == val[0] or wall[s] == val[0]:
            val[1] = val[1] * -1 # flip dir

sum = 0
for c in caught:
    sum += c*wall[c]
print(sum,caught)