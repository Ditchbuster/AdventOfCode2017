with open('input.txt') as f:
    content = f.readlines()
csum = 0
for line in content:
    parts = [int(x) for x in line.split()]
    for p in parts:
        for k in parts:
            if p != k:
                if p%k == 0:
                    csum += int(p/k)
print(csum)