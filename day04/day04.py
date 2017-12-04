with open('input.txt') as f:
    content = f.readlines()
count = 0
for line in content:
    vaild = True
    parts = [x for x in line.split()]
    for i in range(len(parts)):
        if parts[i] in parts[:i:]:
            vaild = False
    if vaild:
        count += 1
print(count)