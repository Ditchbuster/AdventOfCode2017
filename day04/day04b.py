import itertools

with open('input.txt') as f:
    content = f.readlines()
count = 0
for line in content:
    vaild = True
    parts = [x for x in line.split()]
    for i in range(len(parts)):
        perm = itertools.permutations(parts[i])
        for p in perm:
            #print(p)
            p = ''.join(p)
            if p in parts[:i:]:
                vaild = False
    if vaild:
        count += 1
print(count)